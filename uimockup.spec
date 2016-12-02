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
        int skip;
        int trim3;
        int trim5;
        int np;
        int minins;
        int maxins;
        string orientation;
        int min_intron_length;
        int max_intron_length;
        bool no_spliced_alignment;
        bool transcriptome_mapping_only;
        } Hisat2Params;

    typedef structure {
        int num-threads;
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
        string domain;
        bool run_stringtie;
        string genome_id;
        string prefix_output_objects;
        Hisat2Params Hisat2;
        StringTieParams StringTie;
        } Hisat2AndStringTieParams;

    async funcdef Hisat2AndStringTieCall( Hisat2AndStringTieParams params )
                  returns(ResultsToReport) authentication required;





};
