data = load('Ha_Guanf_VL06_2015-02-11_001_01-A_spikes_CH005_SE5a_01_ND.mat');

% Extract values from the fields as cell arrays
trialInBlock = num2cell(data.neuronData.signalValue.trialInBlock(:));
choiceColor = num2cell(data.neuronData.signalValue.choiceColor(:));
choiceLocation = num2cell(data.neuronData.signalValue.choiceLocation(:));
choiceMotionDirection = num2cell(data.neuronData.signalValue.choiceMotionDirection(:));
reward = num2cell(data.neuronData.signalValue.reward(:));
learningStatus = num2cell(data.neuronData.signalValue.learningStatus(:));
HDtrlnum = num2cell(data.neuronData.signalValue.HDtrlnum(:));
probabilityRewardedChoice = num2cell(data.neuronData.signalValue.probabilityRewardedChoice(:));

% Extract values from neuronData.unitInfo
name = cellstr(data.neuronData.unitInfo.name);
iso = cellstr(data.neuronData.unitInfo.iso);
area = cellstr(data.neuronData.unitInfo.area);
probabilityRewardedChoice_unitInfo = num2cell(data.neuronData.unitInfo.probabilityRewardedChoice(:));

% Extract values from neuronData.trialNum
trialNum = num2cell(data.neuronData.trialNum(:));

% Extract values from neuronData.signalTime
stimOn = num2cell(data.neuronData.signalTime.stimOn(:));
colorOnset = num2cell(data.neuronData.signalTime.colorOnset(:));
motionOnset = num2cell(data.neuronData.signalTime.motionOnset(:));
choiceEvent = num2cell(data.neuronData.signalTime.choiceEvent(:));
saccadeChoice = num2cell(data.neuronData.signalTime.saccadeChoice(:));
reward_signalTime = num2cell(data.neuronData.signalTime.reward(:));
f1On = num2cell(data.neuronData.signalTime.f1On(:));
f2On = num2cell(data.neuronData.signalTime.f2On(:));
stimOnTime = num2cell(data.neuronData.signalTime.stimOnTime(:));

% Make all cell arrays the same size by filling with NaN
maxSize = max([numel(name), numel(iso), numel(area), numel(probabilityRewardedChoice_unitInfo), ...
               numel(trialNum), numel(stimOn), numel(colorOnset), numel(motionOnset), ...
               numel(choiceEvent), numel(saccadeChoice), numel(reward_signalTime), numel(f1On), ...
               numel(f2On), numel(stimOnTime)]);

trialInBlock = padToSize(trialInBlock, maxSize, NaN);
choiceColor = padToSize(choiceColor, maxSize, NaN);
choiceLocation = padToSize(choiceLocation, maxSize, NaN);
choiceMotionDirection = padToSize(choiceMotionDirection, maxSize, NaN);
reward = padToSize(reward, maxSize, NaN);
learningStatus = padToSize(learningStatus, maxSize, NaN);
HDtrlnum = padToSize(HDtrlnum, maxSize, NaN);
probabilityRewardedChoice = padToSize(probabilityRewardedChoice, maxSize, NaN);

name = padToSize(name, maxSize);
iso = padToSize(iso, maxSize);
area = padToSize(area, maxSize);
probabilityRewardedChoice_unitInfo = padToSize(probabilityRewardedChoice_unitInfo, maxSize, NaN);
trialNum = padToSize(trialNum, maxSize, NaN);
stimOn = padToSize(stimOn, maxSize, NaN);
colorOnset = padToSize(colorOnset, maxSize, NaN);
motionOnset = padToSize(motionOnset, maxSize, NaN);
choiceEvent = padToSize(choiceEvent, maxSize, NaN);
saccadeChoice = padToSize(saccadeChoice, maxSize, NaN);
reward_signalTime = padToSize(reward_signalTime, maxSize, NaN);
f1On = padToSize(f1On, maxSize, NaN);
f2On = padToSize(f2On, maxSize, NaN);
stimOnTime = padToSize(stimOnTime, maxSize, NaN);

% Create a table with a single row
tableData = table(trialInBlock, choiceColor, choiceLocation, choiceMotionDirection, reward, ...
                  learningStatus, HDtrlnum, probabilityRewardedChoice, name, iso, area, ...
                  probabilityRewardedChoice_unitInfo, trialNum, stimOn, colorOnset, ...
                  motionOnset, choiceEvent, saccadeChoice, reward_signalTime, f1On, f2On, stimOnTime);

% Write the table to a CSV file
outputFileName = [char(name{1}), '_output.csv'];
writetable(tableData, outputFileName);

% Function to pad cell arrays with NaN to a specified size
function paddedArray = padToSize(inputArray, targetSize, fillValue)
    if nargin < 3
        fillValue = NaN;
    end
    paddedArray = cell(targetSize, 1);
    paddedArray(:) = {fillValue};
    paddedArray(1:numel(inputArray)) = inputArray;
end
