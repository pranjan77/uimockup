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
}ResultsToReport;




   typedef structure {
        string ws_id;
        string readset_id;
        string genome_id;
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
        string tailor_alignments;


        bool run_stringtie;
        } Hisat2Params;

  async funcdef Hisat2Call( Hisat2Params params )  returns(ResultsToReport) authentication required;





};
