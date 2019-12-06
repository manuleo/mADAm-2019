function opt_y = QPSolverEuropeAfrica(euc,afc,costs)
%Scaling down values
euc = euc/1e+10;
afc= afc/1e+10;

% define decision variables
y = sdpvar(size(euc,1),size(afc,1),'full');

% define objective function
objective = sum(costs'*y + costs'*y.^2);

% initialize constraints
constraints = [];

% add nonnegativity constraints
constraints = [constraints, y>=0];

%Availability constraint
for j=1:size(euc,1)
    constraints = [constraints, sum(y(j,:)) <= euc(j)];
end

%Demand constraint
for i=1:size(afc,1)
    constraints = [constraints, sum(y(:,i)) == afc(i)];
end

% specify solver settings
opt_settings = sdpsettings('solver', 'gurobi', 'verbose', 0);

% run solver
diagnosis = optimize(constraints, objective, opt_settings);

% display solver report
disp('solver report:');
disp(diagnosis);

% retrieve and display optimal objective value
disp('optimal objective value:');
opt_objective = value(objective);
disp(opt_objective);

% retrieve and display optimal solution values
disp('optimal solution values:');
opt_y = value(y);
disp(opt_y);

%Scaling back values up
opt_y = opt_y*1e+10;
end