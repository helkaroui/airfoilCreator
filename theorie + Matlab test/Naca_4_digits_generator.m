function [ airfoil , camber ] = Naca_4_digits_generator( nacaType , NumberPoints , trailing_edge)
% Inputs:
% nacaType String the naca designation
%Outputs:
% airfoil Matrix The generated airfoil
% camber Matrix The generated camber line

Minit = str2double(nacaType(1));
Pinit = str2double(nacaType(2));
Tinit = str2double(nacaType(3:4));

% Constants used in thickness calculation
a0 = 0.2969;
a1 = -0.1260;
a2 = -0.3516;
a3 = 0.2843;
if (trailing_edge == 0) % Open trailing edge
    a4 = -0.1015;  
elseif(trailing_edge == 1) % Closed trailing edge
    a4 = -0.1036;      
end
        

% Percentage values
M = Minit /100;
P = Pinit /10;
T = Tinit /100;
X = linspace(0,1,NumberPoints)';

% Camber
Yc = ones(NumberPoints,1);
dYc = ones(NumberPoints,1);
theta = ones(NumberPoints,1);
for i=1:NumberPoints
    if (X(i) < P) 
        Yc(i)= (M/P^2)*((2*P*X(i)) - X(i)^2);
        dYc(i) = ((2*M)/(P^2))*(P-X(i));
    elseif (X(i) > P)
        Yc(i)= (M/(1-P)^2)*( 1 - 2*P  + 2*P*X(i) - X(i)^2);
        dYc(i) = ((2*M)/((1-P)^2))*(P-X(i));
    end
    theta(i) = atan(dYc(i));
end
Yt = ones(NumberPoints,1);
Yt = 5*T.*((a0.*sqrt(X)) + (a1.*X) + (a2.*X.^2) + (a3.*X.^3) + (a4.*X.^4));
% Upper Points
Xu = ones(NumberPoints , 1);
Yu = ones(NumberPoints , 1);

Xu = X - Yt.*sin(theta);
Yu = Yc + Yt.*cos(theta);
% Lower Points
Xl = ones(NumberPoints , 1);
Yl = ones(NumberPoints , 1);

Xl = X + Yt.*sin(theta);
Yl = Yc - Yt.*cos(theta);

hold on; grid on;
axis equal;
plot(Xu,Yu,'r-');
plot(Xl,Yl,'b-');
end

