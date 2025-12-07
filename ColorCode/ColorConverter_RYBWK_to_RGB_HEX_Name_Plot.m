%{
Name:
    ColorConverter_RYBWK_to_RGB_HEX_Name_Plot


Version:
    wessler
    2024 September 18
    update to: func_ColorConverter_RYB_to_RGB.m 2024 February 14
    changes:
        *list the closest color

Description:
    *converts an RYB color to RGB


Inputs:
    color_RYB=[R,Y,B] values between 0 (inclusive) and infinity


Outputs/does:
    *converts RYB to RGB
    


Used by:
    NOTHING


Uses:
    NOTHING


NOTES:

inputs:
color_RYB = [R,Y,B,W,K]
0 <= R,Y,B,W,K < inf

these are ratios of colors like paint
Red:Yellow:Blue:White:Black
so:
1:0:0:0:0 means red (primary color)
1:1:0:0:0 means orange (secondary color)
3:1:0:0:0 means vermilion (tertiary color)
1:0:0:1:0 means pink (light red)


color mapping RYB to RGB:
f(R,Y,B) = [R,G,B]
____________________________________________
f(0,0,0)=[1,1,1] (white)
f(0,0,1)=[0.163,0.373,0.6] (blue) [0,0,1]???
f(0,1,0)=[1,1,0] (yellow)
f(0,1,1)=[0,0.66,0.2] (green) [0,1,0]???
f(1,0,0)=[1,0,0] (red)
f(1,0,1)=[0.5,0.5,0]??? (purple)
f(1,1,0)=[1,0.5,0]??? (orange)
f(1,1,1)=[0.2,0.094,0] (brown) 



part of algorithm inspired by:
https://math.stackexchange.com/questions/305395/ryb-and-rgb-color-space-conversion


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%==========================================================================
%--------------------------------------------------------------------------
%__________________________________________________________________________
%}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%inputs
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

R=0;
Y=3;
B=5;
W=0;
K=0;

%--------------------------------------------------------------------------
%check input errors
%--------------------------------------------------------------------------

if R<0||Y<0||B<0||W<0||K<0
    error("All colors must be >= 0!")
end

if sum([R,Y,B,W,K])==0
    error("Must add at least 1 color!")
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%prepare to compute
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%--------------------------------------------------------------------------
% get "ColorListVals" term if not read in yet
%--------------------------------------------------------------------------

if ~exist('ColorList','var')
    if isfile('ColorListVals.csv')
        ColorList=readtable('ColorListVals.csv');
    else
        error("Can't find file to read!")
    end
end


%--------------------------------------------------------------------------
%define corners of RGB cube
%--------------------------------------------------------------------------

white=[1,1,1];
blue=[0.163,0.373,0.6];
blue=[0,0,1];
yellow=[1,1,0];
green=[0,0.66,0.2];
green=[0,1,0];
red=[1,0,0];
purple=[0.5,0,0.5];
orange=[1,0.5,0];
brown=[0.2,0.094,0];


%--------------------------------------------------------------------------
%get relative White/Black values
%--------------------------------------------------------------------------

frac_WK=(W+K)/(R+Y+B+W+K);
if W+K>0
    gray_tint=W/(W+K);
else
    gray_tint=0;
end


%--------------------------------------------------------------------------
%scale RYB to be between 0 and 1 to fit in RYB cube
%--------------------------------------------------------------------------
R_Orig=R;
Y_Orig=Y;
B_Orig=B;

max_val=max([R,Y,B]);
if max_val>0
    R=R/max_val;
    Y=Y/max_val;
    B=B/max_val;
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%convert RGBWK to RGB
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%==========================================================================
%interpolate to convert coordinate in RYB cube to RGB cube
%==========================================================================

RGB = ...
      white *(1-R)*(1-Y)*(1-B)...
    + blue  *(1-R)*(1-Y)*(0+B)...
    + yellow*(1-R)*(0+Y)*(1-B)...
    + green *(1-R)*(0+Y)*(0+B)...
    + red   *(0+R)*(1-Y)*(1-B)...
    + purple*(0+R)*(1-Y)*(0+B)...
    + orange*(0+R)*(0+Y)*(1-B)...
    + brown *(0+R)*(0+Y)*(0+B);


%==========================================================================
%add White/Black
%==========================================================================

RGB=(1-frac_WK)*RGB+frac_WK*gray_tint;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%find HEX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

ActualRGB=round(255*RGB);
HexMat=dec2hex(ActualRGB);
tempstr='000000';
for ii=1:3
    tempHex=HexMat(ii,:);
    if length(tempHex)<2
        str=['0',tempHex];
    else
        str=tempHex;
    end
    tempstr(2*ii-1:2*ii)=str;
end
HexCode=['#',tempstr];


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%find color name
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

tempColor=ColorList(strcmpi(ColorList.HexCode,HexCode)==1,:);
if min(size(tempColor))>0
    FLAG_Match=1;
    tempName=tempColor.ColorName;
    ColorName=tempName{1};
else
    FLAG_Match=0;
    ActualR=ActualRGB(1);
    ActualG=ActualRGB(2);
    ActualB=ActualRGB(3);    
    dim=size(ColorList);
    numColors=dim(1);
    minDist=inf;
    ColorID=NaN;
    for ii=1:numColors
        temp_R=ColorList.RGB_1(ii);
        temp_G=ColorList.RGB_2(ii);
        temp_B=ColorList.RGB_3(ii);
        dist= (ActualR-temp_R)*(ActualR-temp_R) + (ActualG-temp_G)*(ActualG-temp_G) + (ActualB-temp_B)*(ActualB-temp_B);
        if dist<minDist
            minDist=dist;
            ColorID=ii;
        end
    end
    tempName=ColorList.ColorName(ColorID);
    ColorName=tempName{1};
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%display color IDs
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


fprintf('\nRYBWK value [R,Y,B,W,K]:\n[%.3f,%.3f,%.3f,%.3f,%.3f]\n',R_Orig,Y_Orig,B_Orig,W,K)
fprintf('\nRGB color value [R,G,B]:\n[%3.0f,%3.0f,%3.0f]\n',ActualRGB(1),ActualRGB(2),ActualRGB(3))
fprintf('\nHex color value:\n%s\n',HexCode)
if FLAG_Match
    fprintf('\nName of color:\n%s\n',ColorName)
else
    fprintf('\nName of closest color:\n%s\n\n',ColorName)
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%plot color
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

diameter = 2;
xCenter=0;
yCenter=0;

Fig=figure(1);
clf
Plot = rectangle('Position',[xCenter yCenter diameter diameter]);
Axes = gca;

Plot.Curvature=[1,1];
Plot.FaceColor=RGB;
if max(RGB)<1/9
    Plot.EdgeColor=[1,1,1];
elseif min(RGB)>8/9
    Plot.EdgeColor=[0,0,0];
else
    Plot.EdgeColor=RGB;
end

Axes.PlotBoxAspectRatio=[1,1,1];
Axes.XTickLabel=[];
Axes.YTickLabel=[];
Axes.XTick=[];
Axes.YTick=[];
Axes.Title.String=['Color: ',ColorName];
Axes.Title.FontSize=20;






