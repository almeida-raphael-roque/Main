# Central Panel for Daily Routine Execution

This script is a modification of an existing script. It provides an interactive panel for executing daily routines related to generating specific reports. It allows users to either execute individual reports or run all routines at once.

## Features

1. **Delinquency Report**: Generates and processes information about delinquency.
2. **Vehicles Information Report**: Performs ETL (Extract, Transform, Load) for data related to vehicles sets (groups of information).
3. **Active Vehicles Report**: Loads and processes reports for pending plate activations.

The script presents options for the user to select which report they wish to execute or automatically executes all routines after 30 seconds if no choice is made.

## How to Use

### Prerequisites
- Python 3.x installed.
- Required libraries and dependencies configured (check dependencies in the `.py` files for the reports).


### Code Structure
- **`structure_routines()`**: Creates and organizes the available routines.
- **`run_all_routines()`**: Displays the interactive panel and manages the execution of individual or all routines at once.
- **Retry Mechanism**: In case of errors, the system will attempt to execute again up to 3 times.

## Example Usage
```plaintext
Hello, you are in the central panel for executing Daily Routines.

Please check the options below:
----------------------------------------------------------------------------------
1 - DELINQUENCY REPORT
2 - VEHICLES INFORMATION REPORT
3 - ACTIVE VEHICLES REPORT
----------------------------------------------------------------------------------
Which routine would you like to execute? (please type only the number corresponding to the desired routine):
```

- Choose a routine (1, 2, or 3) or let the script execute all routines automatically.

## Logs
The system logs detailed information to track:
- Successes and failures during routine execution.
- Total execution time.

## Project Structure
```plaintext
|-- main.py                    # Main panel for executing routines
|-- relatorio_inadimplencia/
|   |-- ETL.py                 # ETL script for delinquency report
|-- conjuntos_informacoes/
|   |-- ETL.py                 # ETL script for conjunto information report
|-- ativacoes_placas/
|   |-- ETL.py                 # ETL script for pending plate activations
```
