# -*- coding: utf-8 -*-
#BEGIN_HEADER
#END_HEADER


class uimockup:
    '''
    Module Name:
    uimockup

    Module Description:
    A KBase module: uimockup
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    VERSION = "0.0.1"
    GIT_URL = "git@github.com:pranjan77/uimockup.git"
    GIT_COMMIT_HASH = "aaf3c6fa2b034ec4a27ee828d5987229cbee13b0"
    
    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass
    

    def Hisat2Call(self, ctx, params):
        """
        :param params: instance of type "Hisat2Params" -> structure:
           parameter "ws_id" of String, parameter "sampleset_id" of String,
           parameter "genome_id" of String, parameter "num_threads" of Long,
           parameter "quality_score" of String, parameter "skip" of Long,
           parameter "trim3" of Long, parameter "trim5" of Long, parameter
           "np" of Long, parameter "minins" of Long, parameter "maxins" of
           Long, parameter "orientation" of String, parameter
           "min_intron_length" of Long, parameter "max_intron_length" of
           Long, parameter "no_spliced_alignment" of type "bool" (indicates
           true or false values, false <= 0, true >=1), parameter
           "transcriptome_mapping_only" of type "bool" (indicates true or
           false values, false <= 0, true >=1), parameter "tailor_alignments"
           of String
        :returns: instance of type "ResultsToReport" (Object for Report type)
           -> structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN Hisat2Call
        #END Hisat2Call

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method Hisat2Call return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
