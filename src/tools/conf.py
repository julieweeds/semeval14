__author__ = 'juliewe'

def configure(args):

    parameters={}
    parameters['where']='local' #or apollo or athome
    if parameters['where']=='local':
        parameters['parentdir']='/Volumes/LocalScratchHD/juliewe/Documents/workspace'
    parameters['datadir']='semeval2014/traindata'
    parameters['dataset']='trial'
    parameters['datasetdir']='sick_'+parameters['dataset']
    parameters['datasetfile']='SICK_'+parameters['dataset']+'.txt'
    parameters['verbose']=False

    return parameters
