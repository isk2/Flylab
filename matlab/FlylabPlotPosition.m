function FlylabPlotPosition(varargin)
% FlylabPlotPosition(filedata, iFrameParent,iFrameChildren, iTrigger, nSubsample[, iStart, iStop])
% Plot positions of the specified object (robot=1, fly1=2, fly2=3, etc), in the given frame of reference.
% Draws a circle on the sample given by iTrigger.
%

    if nargin==5
        filedata        = varargin{1};
        iFrameParent    = varargin{2};
        iFrameChildren  = varargin{3};
        iTrigger        = varargin{4};              % Index of the trigger rising edge.
        nSubsample      = varargin{5};
        iStart          = 1;                        % Index of the first sample to consider.
        [iStop,n]       = size(filedata.states);    % Index of the last sample to consider.
    elseif nargin==7
        filedata        = varargin{1};
        iFrameParent    = varargin{2};
        iFrameChildren  = varargin{3};
        iTrigger        = varargin{4};
        nSubsample      = varargin{5};
        iStart          = varargin{6};
        iStop           = varargin{7};
    else
        fprintf ('Bad call to FlylabPlotPosition().\nParams are:  FlylabPlotPosition(filedata, iFrameParent,iFrameChildren, iTrigger, nSubsample[, iStart, iStop])\n');
    end
    
    
    % Rotation matrix 90 CCW (so fly is pointing up).
    R90 = [cos(pi/2) -sin(pi/2);
           sin(pi/2)  cos(pi/2)];

    markers = {'o','triangle','triangle','triangle','triangle','triangle','triangle','triangle'};
    colors = [[1.0 0.0 0.0]; 
              [0.3 0.3 0.3]; 
              [0.0 0.8 0.0]; 
              [0.0 0.0 0.8]; 
              [0.0 0.5 0.5]; 
              [0.5 0.0 0.5]; 
              [0.5 0.5 0.0]; 
              [0.3 0.3 0.3]];
    pix = [100 100 100 100 100 100 100 100];
    radii = [0.8 1.25 1.25 1.25 1.25 1.25 1.25 1.25 1.25];
    
    % Start plotting.
    hold off;
    cla;
    axis equal;
    hold on;
    
    for iFrameChild = iFrameChildren
        % Get object pose.
        [pos, ang] = FlylabGetTransformedStates(filedata, iFrameParent, iFrameChild);

        % Rotate if necessary so fly points north.
        if iFrameParent~=0
            pos = (R90 * pos')';   
            ang = ang + pi/2;
        end

        % Subsample vectors for scatter plot.
        x = pos(iStart:nSubsample:iStop, 1);
        y = pos(iStart:nSubsample:iStop, 2);
        ang=ang(iStart:nSubsample:iStop);

        iTriggerA = max(1, floor((iTrigger-iStart+1)/nSubsample));
        xTrig = x(iTriggerA);
        yTrig = y(iTriggerA);
        
        % Remove points outside a boundary.
        if iFrameParent~=0
            rMax = 30;
        else
            rMax = 100000;
        end
        iInBounds = find(x>-rMax & x<rMax & y>-rMax & y<rMax);
        x = x(iInBounds);
        y = y(iInBounds);


        % Draw the  positions, with circles on start and trigger.
        if ~isempty(x)
            scatterPose(x(1),  y(1),    0, radii(iFrameChild), colors(iFrameChild,:), 's', 'none');
            scatterPose(xTrig, yTrig,   0, radii(iFrameChild), colors(iFrameChild,:), 'o', 'none');
            scatterPose(x,     y,     ang, radii(iFrameChild), colors(iFrameChild,:), markers{iFrameChild});
        end

        if iFrameParent~=0
            axis([-rMax rMax -rMax rMax]);
        end
    end
    
    axis off
    axis equal

    