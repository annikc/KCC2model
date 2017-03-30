# KCC2model
Ongoing to-do list: 
https://docs.google.com/document/d/1G1RuNlDHYTx5nhs32q0ZfmgSOhofUhxcbc9QnsA9SNg/edit

This folder contains hoc code for both a single compartment model (in ./SCM) and multicompartment moded (./MCM). 
Both models use mod files from ./_mods

Will update with bash scripts for running code on SciNet system, including automatic compiling from ./_mods

# SCM 
Will focus on getting working simulation in SCM first. To run: 
```
> nrnivmodl ../_mods
> nrngui SCMpromptWindow.hoc
```
Sometimes throws up weird error with bicarb ion. If this happens, delete x86_64 folder (or .o/.c files) and recompile with nrnivmodl. 

## SCMpromptwindow.hoc
Here you set up all the parameters of the induction protocol. Paired synapses are GABAergic synapses which are paired with a postsynaptic spike with some temporal separation (this spike timing interval is set in mosinit.hoc or mosinit_RUNONLY.hoc -- by default it is +5ms i.e. a GABA input followed by a postsynaptic spike 5ms later). 
Synaptic density: the default 0.001 will give one GABA synapse. Since it is a single compartment, all synapses will be placed at the same point. If you change synaptic density you can find out how many synapses are present once you create the cell by typing 
```
> gaba_paired.count()
```
in the terminal window (gaba_paired is a list of all of the gaba_synapses).
Interval between synapse spikes sets the stimulation frequency. By default this is 200 ms  and number of synaptic events is set to 150 to mimic the 5Hz stimulation for 30s in the Woodin 2003 paper. 

Start of synapse spikes is by default 50 ms, in actual simulations we will want it to be ~ 10000 (I previously set to 10050) to allow time for the model to reach its steady state for all variables. 

Clamp parameters are fairly self explanatory. The default values are again meant to mimic those used in Woodin 2003. 

The create cell button calls the necessary hoc files to generate the simulation as you have specified. When the Record Data radio button is unchecked, this will call mosinit_RUNONLY.hoc. When checked, this will call mosinit.hoc. I would recommend not recording data; at this point it's not necessary and I'm not 100% sure it works properly with the SCM at the moment. 

## HOC Files 
Create cell calls the following hoc files:
```
mosinit.hoc or mosinit_RUNONLY.hoc
|   setParameters.hoc
|   makeCell.hoc
    |    makeSingleCompartmentGeometry.hoc
    |    makeIons.hoc
    |    makeTransporters.hoc
    |    makeActiveChannels.hoc
    |    makePairedUnpaired.hoc
|   makeSimpleWindows.hoc
```
You can make changes to any of these files and execute them by clicking the "Create cell" button on the prompt window again. Caveat: for this to work properly you must stop any currently running simulation before recreating the cell. 
If you wish to make changes to any mod files you must completely exit from nrngui, recompile via nrnivmodl (or mknrndll on windows), and then reopen nrngui SCMpromptwindow.hoc. 

Most of the variables you may be interested in changing in the mod files can be changed in setParameters.hoc anyway, so only on rare occassions should you need to change mod files and recompile. 
