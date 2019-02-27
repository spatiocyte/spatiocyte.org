sim = theSimulator.createStepper('SpatiocyteStepper', 'SS')
sim.VoxelRadius = 4.4e-9
theSimulator.rootSystem.StepperID = 'SS'

theSimulator.createEntity('Variable', 'Variable:/:GEOMETRY').Value = 0
theSimulator.createEntity('Variable', 'Variable:/:LENGTHX').Value = 2.5e-7
theSimulator.createEntity('Variable', 'Variable:/:LENGTHY').Value = 2.5e-7
theSimulator.createEntity('Variable', 'Variable:/:LENGTHZ').Value = 2.5e-7

theSimulator.createEntity('Variable', 'Variable:/:XYPLANE').Value = 1
theSimulator.createEntity('Variable', 'Variable:/:XZPLANE').Value = 1
theSimulator.createEntity('Variable', 'Variable:/:YZPLANE').Value = 1

theSimulator.createEntity('Variable', 'Variable:/:VACANT')
theSimulator.createEntity('Variable', 'Variable:/:A').Value = 500
theSimulator.createEntity('Variable', 'Variable:/:B').Value = 500
theSimulator.createEntity('Variable', 'Variable:/:C').Value = 0

populator = theSimulator.createEntity('MoleculePopulateProcess', 'Process:/:pop')
populator.VariableReferenceList = [['_', 'Variable:/:A']]
populator.VariableReferenceList = [['_', 'Variable:/:B']]

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseA')
diffuser.VariableReferenceList = [['_', 'Variable:/:A']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseB')
diffuser.VariableReferenceList = [['_', 'Variable:/:B']]
diffuser.D = 1e-13

diffuser = theSimulator.createEntity('DiffusionProcess', 'Process:/:diffuseC')
diffuser.VariableReferenceList = [['_', 'Variable:/:C']]
diffuser.D = 1e-13

binder = theSimulator.createEntity('DiffusionInfluencedReactionProcess', 'Process:/:reaction1')
binder.VariableReferenceList = [['_', 'Variable:/:A','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:B','-1']]
binder.VariableReferenceList = [['_', 'Variable:/:C','1']]
binder.VariableReferenceList = [['_', 'Variable:/:C','1']]
binder.p = 1

logger = theSimulator.createEntity('VisualizationLogProcess', 'Process:/:logger')
logger.VariableReferenceList = [['_', 'Variable:/:A']]
logger.VariableReferenceList = [['_', 'Variable:/:B']]
logger.VariableReferenceList = [['_', 'Variable:/:C']]

coord = theSimulator.createEntity('CoordinateLogProcess', 'Process:/:coord')
coord.VariableReferenceList = [['_', 'Variable:/:A']]
coord.VariableReferenceList = [['_', 'Variable:/:B']]
coord.VariableReferenceList = [['_', 'Variable:/:C']]

run(0.08)
