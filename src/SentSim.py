__author__ = 'juliewe'

from tools import conf
import sys,os,glob

class Sentence:
    #representation of a sentence in terms of words, lemmas and POS, from .conll representation
    contentTags=['N','V','J','R']

    def __init__(self,id):
        self.fileid=id
        self.positions=[]
        self.words=[]
        self.lemmas=[]
        self.finetags=[]
        self.broadtags=[]
        self.reverselemmas={}
        self.contentlemmas=[]

    def readfile(self,filename):

        with open(filename,'r') as instream:

            for line in instream:
                fields=line.rstrip().split('\t')
                if len(fields)==4:
                    self.positions.append(fields[0])
                    self.words.append(fields[1])
                    self.lemmas.append(fields[2])
                    self.finetags.append(fields[3])
                    broadtag=list(fields[3])[0]
                    self.broadtags.append(broadtag)
                    currentlist=self.reverselemmas.get(fields[2],None)
                    if currentlist==None:
                        self.reverselemmas[fields[2]]=[fields[0]]
                    else:
                        currentlist.append(fields[0])
                        #print currentlist
                        self.reverselemmas[fields[2]]=list(currentlist)
                elif(parameters['verbose']):
                    print "Ignoring "+line
    def displayLemmas(self):
        print(self.lemmas)
        print self.reverselemmas

    def getContentLemmas(self):
        if self.contentlemmas==[]:
            for i,broadtag in enumerate(self.broadtags):
                if broadtag in Sentence.contentTags:
                    self.contentlemmas.append(self.lemmas[i])


        return self.contentlemmas


if __name__=='__main__':
    parameters=conf.configure(sys.argv)
    filedir=os.path.join(parameters['parentdir'],parameters['datadir'],parameters['datasetdir'],'sentences-tagged')
    filesets=['A','B']

    for set in filesets:
        files = glob.glob(os.path.join(filedir,set,'*.conll'))
        count=0
        for afile in files:
            print afile
            parts=afile.split('/')
            fileid=parts[-1].split('.')[0]
            print fileid
            mysentence = Sentence(fileid)
            mysentence.readfile(afile)
            mysentence.displayLemmas()
            print mysentence.getContentLemmas()
            count+=1
            if count%10==0:
                exit()
