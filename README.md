# MQ_PGs_LFQ_general workflow

## Description of the workflow and general remarks
MQ_PGs_LFQ_general is a KNIME workflow developed for the general processing of label-free bottom-up mass spectrometry data.
Please note, that you should understand e.g. data structure and experimental design used within the study to apply the correct processing approach! The processing may require consultation with (bio)statistician to achieve correct outputs.


## Input data
In this workflow, the proteinGroups.txt file, an output of [MaxQuant] (http://coxdocs.org/doku.php?id=maxquant:start) software  is used for the file input. 
In general, the workflow is applicable also to other types of data in wide format data table; please note that additional adjustment of nodes settings may be required then (e.g. different column names, prefixes and suffixes, etc.).

## Documentation of used nodes/metanodes
The workflow contains several nodes for the data processing:
-	File input: proteinGroups.txt table from MaxQuant. The distribution of protein intensities can be visualized for all samples by violin plots and exported as .png file.
-	MQ PGs filtering (e.g. CRAP): metanode for removal of potential protein contaminants (e.g. identified only by site; reverse; potential contaminant; cRAP proteins; ”keratin” keyword containing proteins)
-	Log2 transformation: protein intensities columns undergo logarithmic transformation in order to acquire normal distribution. Columns containing transformed data are appended by default with _log2. The distribution of protein intensities can be visualized for chosen samples by violin plots and exported as .png file. Normalization: There are several normalization techniques which can be used for normalization of protein intensities (log2 transformed)
o	normalization on median (linear)
o	quantile normalization (non-linear)
o	LoessF normalization (non-linear)
o	vsn normalization (non-linear)
Columns containing normalized data are appended by default with _norm. Prior to further processing of the normalized data, e.g. using statistical tests, we recommend visualizing the normalized data by different nodes, e.g. correlation clustermaps, hierarchical clustering, violin plots or scatter plot matrices in order to check the normalized data overall similarity and clustering and in general to choose the most appropriate normalization technique. The images can be subsequently exported as .png file.
-	Log2 back transformation node
-	Statistics: As default statistical test we provide the LIMMA test. Please, adjust the settings and design according to your experimental setup. 
-	Visualization: The results of the LIMMA test are visualized by the volcano plot node; the resulting image can be exported as .png.
-	CSV writer node: whole dataframe is exported as a .csv file

## Additional nodes recommended to use with this workflow
Previously described nodes are what we think is the basis of label-free bottom-up mass spectrometry data processing. However, we recommend using also other nodes for more advanced data processing and evaluation. Here we provide a list of potentially utilized nodes:
-	Missing values imputation node: a strategy for the imputation of missing values by imp4p R package (https://cran.r-project.org/web/packages/imp4p/index.html) is provided. Otherwise, a Value imputation node can be used providing several imputation strategies. The node should be used on log transformed data, prior to data normalization.
-	Upset plot (static/interactive): a plot for displaying the intersections between particular datasets.
-	Volcano plot (interactive): volcano plot in interactive version allowing quick identification of displayed proteins.


