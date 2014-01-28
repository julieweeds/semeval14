from src.tools import conf

__author__ = 'juliewe'
#split the original text file
#produce a gold standard evaluation file containing pair id, GS score and GS relation
#produce one file per sentence (named according to pair id) for input to parser etc

import sys, os

def split(workingdir,infile):

    inpath=os.path.join(workingdir,infile)
    print "Processing "+inpath
    GSout=os.path.join(workingdir,'GS.txt')
    SENTout=os.path.join(workingdir,'sentences')

    with open(inpath,'r') as instream:
        with open(GSout,'w') as gsstream:
            linesread=0
            for line in instream:
                linesread+=1
                if linesread>1: #ignore header line

                    parts=line.rstrip().split('\t') #pairid,s1,s2,degree,relation
                    gsstream.write(parts[0]+'\t'+parts[3]+'\t'+parts[4]+'\n')
                    apath = os.path.join(SENTout,'A',parts[0]+'_A.txt')
                    bpath=os.path.join(SENTout,'B',parts[0]+'_B.txt')
                    with open(apath,'w') as sentstream:
                        sentstream.write(parts[1]+'\n')
                    with open(bpath,'w') as sentstream:
                        sentstream.write(parts[2]+'\n')



if __name__=='__main__':

    parameters= conf.configure(sys.argv)
    filedir=os.path.join(parameters['parentdir'],parameters['datadir'],parameters['datasetdir'])
    split(filedir,parameters['datasetfile'])

