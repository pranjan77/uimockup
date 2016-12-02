/*
A KBase module: uimockup
*/

module uimockup {

/* indicates true or false values, false <= 0, true >=1 */
	typedef int bool; 

/*
     Object for Report type
*/
    typedef structure {
    		string report_name;
		    string report_ref;
        } ResultsToReport;

    typedef structure {
        int num_threads;
        string quality_score;
        int min_intron_length;
        int max_intron_length;
        bool no_spliced_alignment;
        int skip;
        int trim5;
        int trim3;
        int np;
        int minins;
        int maxins;
        string orientation;
        bool transcriptome_mapping_only;
        } Hisat2Params;

    typedef structure {
        string label;
        float min_isoform_abundance;
        int a_juncs;
        int  min_length;
        float j_min_reads;
        float c_min_read_coverage;
        int gap_sep_value;
        bool disable_trimming;
        bool ballgown_mode;
        bool skip_reads_with_no_ref;
        string merge;
        } StringTieParams;


    typedef structure {
        string ws_id;
        string readset_id;
        string genome_id;
        string domain;
        string tailor_alignments;
        bool run_stringtie;
        string prefix_output_objects;
        Hisat2Params Hisat2_grouped_params;
        StringTieParams StringTie2_grouped_params;
        } Hisat2AndStringTieParams;

    async funcdef Hisat2AndStringTieCall( Hisat2AndStringTieParams params )
                  returns(ResultsToReport) authentication required;





};
