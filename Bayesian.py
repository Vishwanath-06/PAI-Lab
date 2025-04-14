from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define CPDs for root nodes B and E
cpd_Burglary = TabularCPD(variable='B', variable_card=2, values=[[0.999], [0.001]])  # P(A)
cpd_Earthquake = TabularCPD(variable='E', variable_card=2, values=[[0.998], [0.002]])  # P(B)

# Step 2: Define CPD for A with parents E and B
cpd_Alarm = TabularCPD(
    variable='A', variable_card=2,
    values=[
        [0.999, 0.71, 0.06, 0.05],  # P(C=False | A, B)
        [0.001, 0.29, 0.94, 0.95]   # P(C=True | A, B)
    ],
    evidence=['B', 'E'],
    evidence_card=[2, 2]
)

# Step 3: Define CPD for M with parents A
cpd_John = TabularCPD(
    variable='J', variable_card=2,
    values=[
        [0.95,0.1],  # P(D=False | B, C)
        [0.05,0.9]   # P(D=True | B, C)
    ],
    evidence=['A'],
    evidence_card=[2]
)

# Step 4: Define CPD for J with parents A
cpd_Mary = TabularCPD(
    variable='M', variable_card=2,
    values=[
        [0.99, 0.3],  # P(E=False | C, D)
        [0.01,0.7]   # P(E=True | C, D)
    ],
    evidence=['A'],
    evidence_card=[2]
)

# Step 5: Define the network structure
model = DiscreteBayesianNetwork([
    ('E', 'A'),
    ('B', 'A'),
    ('A', 'M'),
    ('A', 'J')
])

# Step 6: Add CPDs to the model
model.add_cpds(cpd_Burglary,cpd_Earthquake,cpd_Alarm,cpd_John,cpd_Mary)

# Step 7: Check model validity
assert model.check_model()

# Step 8: Inference engine
inference = VariableElimination(model)

# Step 9: Inference with evidence
print("EarthQuake & Burglary happened but Alarm didn't ring.")
print("What is the probabilties of John & Mary Calling & Not Calling")
evidence = {'A': 0, 'B': 1, 'E': 1}
variables = ['M', 'J']  # Earthquake, MaryCalls, JohnCalls
for var in variables:
    belief = inference.query(variables=[var], evidence=evidence, show_progress=False)
    print(f"{var}:\n{belief}\n")