function header = FlylabReadHeader (filename)
% header = FlylabReadHeader(filename)
% Read the fly & robot state header lines from the given .csv file (as written by Flylab).
% Return a struct containing all the various fields.
%

    fid = fopen(filename);
    
    while (1)
        headings = textscan(fid,'%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q',1,'Delimiter',',');
        switch headings{1}{1}
            case 'versionFile'
                values = textscan(fid,'%q',1,'Delimiter',',');
                for i=1:length(values)
                    if strcmpi(values{i},'True'); values{i}=true; end;
                    if strcmpi(values{i},'False'); values{i}=false; end;
                end
                if str2num(values{1}{1})<2.81
                    fprintf('WARNING: This code only reads Flylab .csv version 2.81\nUse ConvertCsv.py to convert.\n');
                    % Note: to update for newer versions, change the
                    % textscan() lines below to accommodate the changed
                    % header lines.
                end
                structVersion = struct(headings{1}{1},values{1});
                
            
            case 'date_time'
                values = textscan(fid,'%f%q%d%d',1,'Delimiter',',');
                for i=1:length(values)
                    if strcmpi(values{i},'True'); values{i}=true; end;
                    if strcmpi(values{i},'False'); values{i}=false; end;
                end
                structTop = struct(headings{1}{1},values{1}, ...
                                   headings{2}{1},values{2}, ...
                                   headings{3}{1},values{3}, ...
                                   headings{4}{1},values{4});
                
            case 'nRobots'
                values = textscan(fid,'%d%f%f%q%q%q',1,'Delimiter',',');
                for i=1:length(values)
                    if strcmpi(values{i},'True'); values{i}=true; end;
                    if strcmpi(values{i},'False'); values{i}=false; end;
                end
                structRobots = struct(headings{1}{1},values{1}, ...
                                   headings{2}{1},values{2}, ...
                                   headings{3}{1},values{3}, ...
                                   headings{4}{1},values{4}, ...
                                   headings{5}{1},values{5}, ...
                                   headings{6}{1},values{6});
                
            case 'nFlies'
                values = textscan(fid,'%d%q%q',1,'Delimiter',',');
                for i=1:length(values)
                    if strcmpi(values{i},'True'); values{i}=true; end;
                    if strcmpi(values{i},'False'); values{i}=false; end;
                end
                structFlies = struct(headings{1}{1},values{1}, ...
                                   headings{2}{1},values{2}, ...
                                   headings{3}{1},values{3});
                
            case 'trackingExclusionzoneEnabled'
                values = textscan(fid,'%q%f%f%f',1,'Delimiter',',');
                for i=1:length(values)
                    if strcmpi(values{i},'True'); values{i}=true; end;
                    if strcmpi(values{i},'False'); values{i}=false; end;
                end
                structTrackingExclusionzone = struct(headings{1}{1},values{1}, ...
                                   headings{2}{1},values{2}, ...
                                   headings{3}{1},values{3}, ...
                                   headings{4}{1},values{4});
                
            case 'preRobotEnabled'
                values = textscan(fid,'%q%q%q%q%f%f%d%f%f%f%d%q%q%q%f%f%q%f%q%f',1,'Delimiter',',');
                for i=1:length(values)
                    if strcmpi(values{i},'True'); values{i}=true; end;
                    if strcmpi(values{i},'False'); values{i}=false; end;
                end
                structPreRobot = struct(headings{1}{1},values{1}, ...
                                   headings{2}{1},values{2}, ...
                                   headings{3}{1},values{3}, ...
                                   headings{4}{1},values{4}, ...
                                   headings{5}{1},values{5}, ...
                                   headings{6}{1},values{6}, ...
                                   headings{7}{1},values{7}, ...
                                   headings{8}{1},values{8}, ...
                                   headings{9}{1},values{9}, ...
                                   headings{10}{1},values{10}, ...
                                   headings{11}{1},values{11}, ...
                                   headings{12}{1},values{12}, ...
                                   headings{13}{1},values{13}, ...
                                   headings{14}{1},values{14}, ...
                                   headings{15}{1},values{15}, ...
                                   headings{16}{1},values{16}, ...
                                   headings{17}{1},values{17}, ...
                                   headings{18}{1},values{18}, ...
                                   headings{19}{1},values{19}, ...
                                   headings{20}{1},values{20});

            case 'preLaserEnabled'
                values = textscan(fid,'%q%q%q%q%f%f%d%f%f%f%d%q%q%q',1,'Delimiter',',');
                for i=1:length(values)
                    if strcmpi(values{i},'True'); values{i}=true; end;
                    if strcmpi(values{i},'False'); values{i}=false; end;
                end
                structPreLaser = struct(headings{1}{1},values{1}, ...
                                   headings{2}{1},values{2}, ...
                                   headings{3}{1},values{3}, ...
                                   headings{4}{1},values{4}, ...
                                   headings{5}{1},values{5}, ...
                                   headings{6}{1},values{6}, ...
                                   headings{7}{1},values{7}, ...
                                   headings{8}{1},values{8}, ...
                                   headings{9}{1},values{9}, ...
                                   headings{10}{1},values{10}, ...
                                   headings{11}{1},values{11}, ...
                                   headings{12}{1},values{12}, ...
                                   headings{13}{1},values{13}, ...
                                   headings{14}{1},values{14});

            case 'preLEDPanelsEnabled'
                values = textscan(fid,'%q%q%d%q%q%q%q',1,'Delimiter',',');
                for i=1:length(values)
                    if strcmpi(values{i},'True'); values{i}=true; end;
                    if strcmpi(values{i},'False'); values{i}=false; end;
                end
                structPreLEDPanels = struct(headings{1}{1},values{1}, ...
                                   headings{2}{1},values{2}, ...
                                   headings{3}{1},values{3}, ...
                                   headings{4}{1},values{4}, ...
                                   headings{5}{1},values{5}, ...
                                   headings{6}{1},values{6}, ...
                                   headings{7}{1},values{7});
                
            case 'preWait1'
                values = textscan(fid,'%f',1,'Delimiter',',');
                for i=1:length(values)
                    if strcmpi(values{i},'True'); values{i}=true; end;
                    if strcmpi(values{i},'False'); values{i}=false; end;
                end
                structPreWait1 = struct(headings{1}{1},values{1});
                
            case 'preTriggerEnabled'
                values = textscan(fid,'%q%q%q%f%f%f%f%f%f%f%f%f%f%q%q%f%f',1,'Delimiter',',');
                for i=1:length(values)
                    if strcmpi(values{i},'True'); values{i}=true; end;
                    if strcmpi(values{i},'False'); values{i}=false; end;
                end
                structPreTrigger = struct(headings{1}{1},values{1}, ...
                                   headings{2}{1},values{2}, ...
                                   headings{3}{1},values{3}, ...
                                   headings{4}{1},values{4}, ...
                                   headings{5}{1},values{5}, ...
                                   headings{6}{1},values{6}, ...
                                   headings{7}{1},values{7}, ...
                                   headings{8}{1},values{8}, ...
                                   headings{9}{1},values{9}, ...
                                   headings{10}{1},values{10}, ...
                                   headings{11}{1},values{11}, ...
                                   headings{12}{1},values{12}, ...
                                   headings{13}{1},values{13}, ...
                                   headings{14}{1},values{14}, ...
                                   headings{15}{1},values{15}, ...
                                   headings{16}{1},values{16}, ...
                                   headings{17}{1},values{17});
                
            case 'preWait2'
                values = textscan(fid,'%f',1,'Delimiter',',');
                for i=1:length(values)
                    if strcmpi(values{i},'True'); values{i}=true; end;
                    if strcmpi(values{i},'False'); values{i}=false; end;
                end
                structPreWait2 = struct(headings{1}{1},values{1});
                
            case 'trialRobotEnabled'
                values = textscan(fid,'%q%q%q%q%f%f%d%f%f%f%d%q%q%q%f%f%q%f%q%f',1,'Delimiter',',');
                for i=1:length(values)
                    if strcmpi(values{i},'True'); values{i}=true; end;
                    if strcmpi(values{i},'False'); values{i}=false; end;
                end
                structTrialRobot = struct(headings{1}{1},values{1}, ...
                                   headings{2}{1},values{2}, ...
                                   headings{3}{1},values{3}, ...
                                   headings{4}{1},values{4}, ...
                                   headings{5}{1},values{5}, ...
                                   headings{6}{1},values{6}, ...
                                   headings{7}{1},values{7}, ...
                                   headings{8}{1},values{8}, ...
                                   headings{9}{1},values{9}, ...
                                   headings{10}{1},values{10}, ...
                                   headings{11}{1},values{11}, ...
                                   headings{12}{1},values{12}, ...
                                   headings{13}{1},values{13}, ...
                                   headings{14}{1},values{14}, ...
                                   headings{15}{1},values{15}, ...
                                   headings{16}{1},values{16}, ...
                                   headings{17}{1},values{17}, ...
                                   headings{18}{1},values{18}, ...
                                   headings{19}{1},values{19}, ...
                                   headings{20}{1},values{20});
                
            case 'trialLaserEnabled'
                values = textscan(fid,'%q%q%q%q%f%f%d%f%f%f%d%q%q%q',1,'Delimiter',',');
                for i=1:length(values)
                    if strcmpi(values{i},'True'); values{i}=true; end;
                    if strcmpi(values{i},'False'); values{i}=false; end;
                end
                structTrialLaser = struct(headings{1}{1},values{1}, ...
                                   headings{2}{1},values{2}, ...
                                   headings{3}{1},values{3}, ...
                                   headings{4}{1},values{4}, ...
                                   headings{5}{1},values{5}, ...
                                   headings{6}{1},values{6}, ...
                                   headings{7}{1},values{7}, ...
                                   headings{8}{1},values{8}, ...
                                   headings{9}{1},values{9}, ...
                                   headings{10}{1},values{10}, ...
                                   headings{11}{1},values{11}, ...
                                   headings{12}{1},values{12}, ...
                                   headings{13}{1},values{13}, ...
                                   headings{14}{1},values{14});
                
            case 'trialLEDPanelsEnabled'
                values = textscan(fid,'%q%q%d%q%q%q%q',1,'Delimiter',',');
                for i=1:length(values)
                    if strcmpi(values{i},'True'); values{i}=true; end;
                    if strcmpi(values{i},'False'); values{i}=false; end;
                end
                structTrialLEDPanels = struct(headings{1}{1},values{1}, ...
                                   headings{2}{1},values{2}, ...
                                   headings{3}{1},values{3}, ...
                                   headings{4}{1},values{4}, ...
                                   headings{5}{1},values{5}, ...
                                   headings{6}{1},values{6}, ...
                                   headings{7}{1},values{7});

            
            case 'postTriggerEnabled'
                values = textscan(fid,'%q%q%q%f%f%f%f%f%f%f%f%f%f%q%q%f%f',1,'Delimiter',',');
                for i=1:length(values)
                    if strcmpi(values{i},'True'); values{i}=true; end;
                    if strcmpi(values{i},'False'); values{i}=false; end;
                end
                structPostTrigger = struct(headings{1}{1},values{1}, ...
                                   headings{2}{1},values{2}, ...
                                   headings{3}{1},values{3}, ...
                                   headings{4}{1},values{4}, ...
                                   headings{5}{1},values{5}, ...
                                   headings{6}{1},values{6}, ...
                                   headings{7}{1},values{7}, ...
                                   headings{8}{1},values{8}, ...
                                   headings{9}{1},values{9}, ...
                                   headings{10}{1},values{10}, ...
                                   headings{11}{1},values{11}, ...
                                   headings{12}{1},values{12}, ...
                                   headings{13}{1},values{13}, ...
                                   headings{14}{1},values{14}, ...
                                   headings{15}{1},values{15}, ...
                                   headings{16}{1},values{16}, ...
                                   headings{17}{1},values{17});
                
            case 'postWait'
                values = textscan(fid,'%f',1,'Delimiter',',');
                for i=1:length(values)
                    if strcmpi(values{i},'True'); values{i}=true; end;
                    if strcmpi(values{i},'False'); values{i}=false; end;
                end
                structPostWait = struct(headings{1}{1},values{1});
                
            case 'time'
                break
        end
    end
 
    % Build the output structure.
    header = struct();
    topfields = fieldnames(structTop);
    for i = 1:length(topfields)
        header = setfield(header, topfields{i}, getfield(structTop,topfields{i}));
    end
    header.version               = structVersion;
    header.robots                = structRobots;
    header.flies                 = structFlies;
    header.trackingExclusionzone = structTrackingExclusionzone;
    header.preRobot              = structPreRobot;
    header.preLaser              = structPreLaser;
    header.preLEDPanels          = structPreLEDPanels;
    header.preWait1              = structPreWait1;
    header.preTrigger            = structPreTrigger;
    header.preWait2              = structPreWait2;
    header.trialRobot            = structTrialRobot;
    header.trialLaser            = structTrialLaser;
    header.trialLEDPanels        = structTrialLEDPanels;
    header.postTrigger           = structPostTrigger;
    header.postWait              = structPostWait;
    
    fclose(fid);
                
