
clc;
clear;
close all;

%% Problem Definition

CostFunction = @(x) ackley(x);    % Cost Function

nPop = 5;            % Number of Decision Variables

VarSize = [1 nPop];   % Decision Variables Matrix Size

VarMin = -5;          % Lower Bound of Decision Variables
VarMax = 5;          % Upper Bound of Decision Variables

%% DE Parameters

MaxIt = 1000;      % Maximum Number of Iterations

nPop = 50;        % Population Size


CR = 0.2;        % Crossover Probability
F=0.8;             %
%% Initialization

empty_individual.Position = [];
empty_individual.Cost = [];

BestSol.Cost = inf;

pop = repmat(empty_individual, nPop, 1);

for i = 1:nPop

    pop(i).Position = unifrnd(VarMin, VarMax, VarSize);
    
    pop(i).Cost = CostFunction(pop(i).Position);
    
    if pop(i).Cost<BestSol.Cost
        BestSol = pop(i);
    end
    
end

BestCost = zeros(MaxIt, 1);

%% DE Main Loop

for it = 1:MaxIt
    
    for i = 1:nPop
        
        x = pop(i).Position;
        
        A = randperm(nPop);
        
        A(A == i) = [];
        
        r1 = A(1);
        r2 = A(2);
        r3 = A(3);
        
        % Mutation
        
        v = pop(r1).Position+F.*(pop(r2).Position-pop(r3).Position);
        v = max(v, VarMin);
		v = min(v, VarMax);
		
        % Crossover
        u = zeros(size(x));
        j0 = randi([1 numel(x)]);
        for j = 1:numel(x)
            if j == j0 || rand <= CR
                u(j) = v(j);
            else
                u(j) = x(j);
            end
        end
        
        NewSol.Position = u;
        NewSol.Cost = CostFunction(NewSol.Position);
        
        % Selection
        if NewSol.Cost<pop(i).Cost
            pop(i) = NewSol;
            
            if pop(i).Cost<BestSol.Cost
               BestSol = pop(i);
            end
        end
        
    end
    
    % Update Best Cost
    BestCost(it) = BestSol.Cost;
    
    % Show Iteration Information
    disp(['Iteration ' num2str(it) ': Best Cost = ' num2str(BestCost(it))]);
    
end

%% Show Results

figure;
%plot(BestCost);
semilogy(BestCost, 'LineWidth', 2);
xlabel('Iteration');
ylabel('Best Cost');
grid on;
