function FlylabPlotHistogramPosition(filedata, iFrameParent, iFrameChild, radius, nBins)
% FlylabPlotPositionHistogram(filedata, iFrameParent, iFrameChild)
% Plot a heatmap of where the fly has been.
%
%

    nClipped = 150;

    histogram = FlylabGetHistogramPosition(filedata, iFrameParent, iFrameChild, radius, nBins);
    %histogram = FlylabClipByCount(histogram, nClipped);

    % Make the histogram into an image, i.e. normalize to 1.
    img = histogram ./ max(max(histogram));  


    kernIdentity = [.00 .00  .00  .00  .00 .00 .00;
                    .00 .00  .00  .00  .00 .00 .00;
                    .00 .00  .00  .00  .00 .00 .00;
                    .00 .00  .00 1.00  .00 .00 .00;
                    .00 .00  .00  .00  .00 .00 .00;
                    .00 .00  .00  .00  .00 .00 .00;
                    .00 .00  .00  .00  .00 .00 .00];

    kernBlur = [.00 .00  .00  .05  .00 .00 .00;
                .00 .05  .18  .32  .18 .05 .00;
                .00 .18  .64 1.00  .64 .18 .00;
                .05 .32 1.00 1.00 1.00 .32 .05;
                .00 .18  .64 1.00  .64 .18 .00;
                .00 .05  .18  .32  .18 .05 .00;
                .00 .00  .00  .05  .00 .00 .00];
    kernBlur = kernBlur / sum(sum(kernBlur));

    % Make color values match with the colormap, and rotate 90 twice.
    imgIdent = rot90(conv2(img,kernIdentity)*length(hot),2);
    imgBlur = rot90(conv2(img,kernBlur)*length(hot),2);
    
    clf;
    subplot(1,2,1);
    hold off;
    cla;
    image(imgIdent); 
    hold on; [m n]=size(imgIdent); scatterPose(n/2,m/2,pi/2,[1,1,1],10,'triangle');
    colormap(hot);
    axis equal
    axis([0 nBins 0 nBins]);
    axis xy;
    title('Raw Histogram');

    subplot(1,2,2);
    hold off;
    image(imgBlur); 
    hold on; [m n]=size(imgBlur); scatterPose(n/2,m/2,pi/2,[1,1,1],10,'triangle');
    colormap(hot);
    axis equal
    axis([0 nBins 0 nBins]);
    axis xy;
    title('Blurred Histogram');

    