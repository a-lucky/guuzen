# encoding: utf-8
# module _MeCab
# by generator 1.138
# no doc
# no imports

# Variables with simple values

MECAB_ALLOCATE_SENTENCE = 64

MECAB_ALL_MORPHS = 32

MECAB_ALTERNATIVE = 16

MECAB_ANY_BOUNDARY = 0

MECAB_BOS_NODE = 2

MECAB_EON_NODE = 4

MECAB_EOS_NODE = 3

MECAB_INSIDE_TOKEN = 2

MECAB_MARGINAL_PROB = 8

MECAB_NBEST = 2

MECAB_NOR_NODE = 0

MECAB_ONE_BEST = 1

MECAB_PARTIAL = 4

MECAB_SYS_DIC = 0

MECAB_TOKEN_BOUNDARY = 1

MECAB_UNK_DIC = 2
MECAB_UNK_NODE = 1

MECAB_USR_DIC = 1

VERSION = '0.996'

# functions

def delete_DictionaryInfo(*args, **kwargs): # real signature unknown
    pass

def delete_Lattice(*args, **kwargs): # real signature unknown
    pass

def delete_Model(*args, **kwargs): # real signature unknown
    pass

def delete_Tagger(*args, **kwargs): # real signature unknown
    pass

def DictionaryInfo_charset_get(*args, **kwargs): # real signature unknown
    pass

def DictionaryInfo_filename_get(*args, **kwargs): # real signature unknown
    pass

def DictionaryInfo_lsize_get(*args, **kwargs): # real signature unknown
    pass

def DictionaryInfo_next_get(*args, **kwargs): # real signature unknown
    pass

def DictionaryInfo_rsize_get(*args, **kwargs): # real signature unknown
    pass

def DictionaryInfo_size_get(*args, **kwargs): # real signature unknown
    pass

def DictionaryInfo_swigregister(*args, **kwargs): # real signature unknown
    pass

def DictionaryInfo_type_get(*args, **kwargs): # real signature unknown
    pass

def DictionaryInfo_version_get(*args, **kwargs): # real signature unknown
    pass

def Lattice_add_request_type(*args, **kwargs): # real signature unknown
    pass

def Lattice_begin_nodes(*args, **kwargs): # real signature unknown
    pass

def Lattice_bos_node(*args, **kwargs): # real signature unknown
    pass

def Lattice_boundary_constraint(*args, **kwargs): # real signature unknown
    pass

def Lattice_clear(*args, **kwargs): # real signature unknown
    pass

def Lattice_end_nodes(*args, **kwargs): # real signature unknown
    pass

def Lattice_enumNBestAsString(*args, **kwargs): # real signature unknown
    pass

def Lattice_eos_node(*args, **kwargs): # real signature unknown
    pass

def Lattice_feature_constraint(*args, **kwargs): # real signature unknown
    pass

def Lattice_has_constraint(*args, **kwargs): # real signature unknown
    pass

def Lattice_has_request_type(*args, **kwargs): # real signature unknown
    pass

def Lattice_is_available(*args, **kwargs): # real signature unknown
    pass

def Lattice_newNode(*args, **kwargs): # real signature unknown
    pass

def Lattice_next(*args, **kwargs): # real signature unknown
    pass

def Lattice_remove_request_type(*args, **kwargs): # real signature unknown
    pass

def Lattice_request_type(*args, **kwargs): # real signature unknown
    pass

def Lattice_sentence(*args, **kwargs): # real signature unknown
    pass

def Lattice_set_boundary_constraint(*args, **kwargs): # real signature unknown
    pass

def Lattice_set_feature_constraint(*args, **kwargs): # real signature unknown
    pass

def Lattice_set_request_type(*args, **kwargs): # real signature unknown
    pass

def Lattice_set_result(*args, **kwargs): # real signature unknown
    pass

def Lattice_set_sentence(*args, **kwargs): # real signature unknown
    pass

def Lattice_set_theta(*args, **kwargs): # real signature unknown
    pass

def Lattice_set_what(*args, **kwargs): # real signature unknown
    pass

def Lattice_set_Z(*args, **kwargs): # real signature unknown
    pass

def Lattice_size(*args, **kwargs): # real signature unknown
    pass

def Lattice_swigregister(*args, **kwargs): # real signature unknown
    pass

def Lattice_theta(*args, **kwargs): # real signature unknown
    pass

def Lattice_toString(*args, **kwargs): # real signature unknown
    pass

def Lattice_what(*args, **kwargs): # real signature unknown
    pass

def Lattice_Z(*args, **kwargs): # real signature unknown
    pass

def Model_create(*args, **kwargs): # real signature unknown
    pass

def Model_createLattice(*args, **kwargs): # real signature unknown
    pass

def Model_createTagger(*args, **kwargs): # real signature unknown
    pass

def Model_dictionary_info(*args, **kwargs): # real signature unknown
    pass

def Model_lookup(*args, **kwargs): # real signature unknown
    pass

def Model_swap(*args, **kwargs): # real signature unknown
    pass

def Model_swigregister(*args, **kwargs): # real signature unknown
    pass

def Model_transition_cost(*args, **kwargs): # real signature unknown
    pass

def Model_version(*args, **kwargs): # real signature unknown
    pass

def new_DictionaryInfo(*args, **kwargs): # real signature unknown
    pass

def new_Lattice(*args, **kwargs): # real signature unknown
    pass

def new_Model(*args, **kwargs): # real signature unknown
    pass

def new_Tagger(*args, **kwargs): # real signature unknown
    pass

def Node_alpha_get(*args, **kwargs): # real signature unknown
    pass

def Node_beta_get(*args, **kwargs): # real signature unknown
    pass

def Node_bnext_get(*args, **kwargs): # real signature unknown
    pass

def Node_char_type_get(*args, **kwargs): # real signature unknown
    pass

def Node_cost_get(*args, **kwargs): # real signature unknown
    pass

def Node_enext_get(*args, **kwargs): # real signature unknown
    pass

def Node_feature_get(*args, **kwargs): # real signature unknown
    pass

def Node_id_get(*args, **kwargs): # real signature unknown
    pass

def Node_isbest_get(*args, **kwargs): # real signature unknown
    pass

def Node_lcAttr_get(*args, **kwargs): # real signature unknown
    pass

def Node_length_get(*args, **kwargs): # real signature unknown
    pass

def Node_lpath_get(*args, **kwargs): # real signature unknown
    pass

def Node_next_get(*args, **kwargs): # real signature unknown
    pass

def Node_posid_get(*args, **kwargs): # real signature unknown
    pass

def Node_prev_get(*args, **kwargs): # real signature unknown
    pass

def Node_prob_get(*args, **kwargs): # real signature unknown
    pass

def Node_prob_set(*args, **kwargs): # real signature unknown
    pass

def Node_rcAttr_get(*args, **kwargs): # real signature unknown
    pass

def Node_rlength_get(*args, **kwargs): # real signature unknown
    pass

def Node_rpath_get(*args, **kwargs): # real signature unknown
    pass

def Node_stat_get(*args, **kwargs): # real signature unknown
    pass

def Node_surface_get(*args, **kwargs): # real signature unknown
    pass

def Node_swigregister(*args, **kwargs): # real signature unknown
    pass

def Node_wcost_get(*args, **kwargs): # real signature unknown
    pass

def Path_cost_get(*args, **kwargs): # real signature unknown
    pass

def Path_lnext_get(*args, **kwargs): # real signature unknown
    pass

def Path_lnode_get(*args, **kwargs): # real signature unknown
    pass

def Path_prob_get(*args, **kwargs): # real signature unknown
    pass

def Path_prob_set(*args, **kwargs): # real signature unknown
    pass

def Path_rnext_get(*args, **kwargs): # real signature unknown
    pass

def Path_rnode_get(*args, **kwargs): # real signature unknown
    pass

def Path_swigregister(*args, **kwargs): # real signature unknown
    pass

def SWIG_PyInstanceMethod_New(*args, **kwargs): # real signature unknown
    pass

def Tagger_all_morphs(*args, **kwargs): # real signature unknown
    pass

def Tagger_create(*args, **kwargs): # real signature unknown
    pass

def Tagger_dictionary_info(*args, **kwargs): # real signature unknown
    pass

def Tagger_formatNode(*args, **kwargs): # real signature unknown
    pass

def Tagger_lattice_level(*args, **kwargs): # real signature unknown
    pass

def Tagger_next(*args, **kwargs): # real signature unknown
    pass

def Tagger_nextNode(*args, **kwargs): # real signature unknown
    pass

def Tagger_parse(*args, **kwargs): # real signature unknown
    pass

def Tagger_parseNBest(*args, **kwargs): # real signature unknown
    pass

def Tagger_parseNBestInit(*args, **kwargs): # real signature unknown
    pass

def Tagger_parseToNode(*args, **kwargs): # real signature unknown
    pass

def Tagger_parseToString(*args, **kwargs): # real signature unknown
    pass

def Tagger_partial(*args, **kwargs): # real signature unknown
    pass

def Tagger_request_type(*args, **kwargs): # real signature unknown
    pass

def Tagger_set_all_morphs(*args, **kwargs): # real signature unknown
    pass

def Tagger_set_lattice_level(*args, **kwargs): # real signature unknown
    pass

def Tagger_set_partial(*args, **kwargs): # real signature unknown
    pass

def Tagger_set_request_type(*args, **kwargs): # real signature unknown
    pass

def Tagger_set_theta(*args, **kwargs): # real signature unknown
    pass

def Tagger_swigregister(*args, **kwargs): # real signature unknown
    pass

def Tagger_theta(*args, **kwargs): # real signature unknown
    pass

def Tagger_version(*args, **kwargs): # real signature unknown
    pass

def Tagger_what(*args, **kwargs): # real signature unknown
    pass

# no classes
