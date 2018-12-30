# KNIME_workflows
KNIME_workflows repository contains workflows for [KNIME](https://www.knime.com/) analytics platform primarily for the processing of mass-spectrometry-based proteomics data.


## How to use the KNIME workflows
In workflows we aim to provide the most important nodes for the processing of a particular experiment type, including nodes for data transformation, normalization, quality controls, statistical tests and subsequent visualization. At the same time, we encourage the users to accommodate the workflow according to their personal needs and specificity of the processed dataset. Additional nodes can be incorporated in any part of the given workflow. For the use of [metanodes ]( https://github.com/OmicsWorkflows/KNIME_metanodes) in the KNIME workflows please follow the respective [readme file](https://github.com/OmicsWorkflows/KNIME_metanodes/blob/master/README.md) and metanodes description.


To use the KNIME workflow please follow these steps:
1)	download the actual version of all workflows (folder ‘_Workflows templates’) or just individual workflow’s folder
2)	move workflow(s) copy into your KNIME workspace folder (e.g. 'D:\knime-workspace\' on Windows or '/home/user/knime-workspace' on linux)
3)	start KNIME; in case the KNIME is already running, refresh the KNIME workspace to refresh the workspace content (right click on the workspace in the KNIME Explorer sub-window and select Refresh)
4)	double click on the workflow you want to use to open it
5)	save the workflow under the new name
6)	double click on the particular node/metanode to get form window, adjust individual settings and run it.
7)	Use additional nodes/metanodes to adjust the workflow to meet yours and dataset requirements.

## General workflows features
- workflows are versioned individually
    - current workflows versions are in “_Workflows templates” folder, older versions are in “_Workflows templates - older ”
- workflows  are optimized for usage in docker container running KNIME ([KNIME_docker_vnc](https://github.com/OmicsWorkflows/KNIME_docker_vnc)) that should make them reproducible


## Workflows preparation guidelines
We make KNIME workflows having the following guidelines in mind :
-	Workflows should be easy to be used also by a user with no programming/scripting skills
-	Workflows aim to make more complicated operations in KNIME easier and reproducible together with KNIME metanodes
-	Workflows utilize preferably in-built KNIME metanodes but also in-house developed [metanodes](https://github.com/OmicsWorkflows/KNIME_metanodes)
-	Workflows should contain   nodes or metanodes for all commonly used processing steps for a concrete type of proteomic data (e.g. bottom-up label-free data) and experimental design; at the same time the workflow should be easily modifiable according to user’s particular needs/requirements
-	Workflows are built to facilitate interactive, flexible and not unsupervised  way of data processing pipelines
-	Workflows should be well documented both within the KNIME and in respective readme files of each workflow. The readme file should contain:
    -	Workflow description including the purpose of the whole pipeline
    -	Description of data which can be utilized within the workflow
    -	Documentation of all essential and recommended nodes and metanodes
-	Image of the particular workflow

## List  of used programs and extensions and the respective licenses
Workflows are made within docker container running KNIME accessible via [VNC](https://github.com/OmicsWorkflows/KNIME_docker_vnc). Please, check the respective [readme file]( https://github.com/OmicsWorkflows/KNIME_docker_vnc/blob/master/README.md) for more information on the used programs and the respective licenses.

## Do you have a question or want to get involved?
The project is maintained by people from several laboratories (see below), but each workflow has a 'contact person' who should be contacted first in the case of any question. See readme file   for the concrete workflow or workflow annotation. You can also [create an issue here](https://github.com/OmicsWorkflows/KNIME_workflows/issues/new).

If you want to contribute to the project, contact us at david.potesil@ceitec.muni.cz.

### Code of Conduct
This project and everyone participating in it is governed by the [Code of Conduct](../master/code-of-conduct.md). By participating, you are expected to uphold this code. Please report any unacceptable behavior.

# Contributors

The project is maintained by people from several laboratories (in alphabetical order):
- [Laboratory of cellular communication](http://www.sci.muni.cz/bryjalab/), Department of Experimental Biology, Faculty of Science, Masaryk University, Brno, Czech Republic
  - Kristína Gömöryová
- [Proteomics Research group](https://www.ceitec.eu/proteomics-zbynek-zdrahal/rg49), Central European Institute of Technology, Masaryk University, Brno, Czech Republic
  - David Potěšil

# License
Workflows are available under the GNU GPL 3.0 License (see the [LICENSE](../master/LICENSE) file for details), unless stated otherwise.


