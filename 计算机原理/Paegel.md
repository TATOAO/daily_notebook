

# Langchain Pregel

Pregel combines actors and channels into a single application. Actors read data from channels and write data to channels. Pregel organizes the execution of the application into multiple steps, following the Pregel Algorithm/Bulk Synchronous Parallel model.

Each step consists of three phases:

1. Plan: Determine which actors to execute in this step. 
For example, 
a). in the first step, select the actors that subscribe to the special input channels; 
b). in subsequent steps, select the actors that subscribe to channels updated in the previous step.

2. Execution: Execute all selected actors in parallel, until all complete, or one fails, or a timeout is reached. During this phase, channel updates are invisible to actors until the next step.

3. Update: Update the channels with the values written by the actors in this step.
Repeat until no actors are selected for execution, or a maximum number of steps is reached.

