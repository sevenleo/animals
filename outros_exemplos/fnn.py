from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer

from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal


means = [(-1,0),(2,4),(3,1)]

cov = [diag([1,1]), diag([0.5,1.2]), diag([1.5,0.7])]

alldata = ClassificationDataSet(2, 1, nb_classes=3)

for n in xrange(500):
    for klass in range(3):
        #input = multivariate_normal(means[klass])
        #input = multivariate_normal(means[klass],cov[klass])
        alldata.addSample(means[klass], [klass])


tstdata, trndata = alldata.splitWithProportion( 0.25 )
trndata._convertToOneOfMany( )
tstdata._convertToOneOfMany( )

print "____________________________________________________________________________"
print "Number of training patterns: ", len(trndata)
print "Input and output dimensions: ", trndata.indim, trndata.outdim
print "First sample (input, target, class):"
print trndata['input'][0], trndata['target'][0], trndata['class'][0]
print "____________________________________________________________________________\n"



fnn = buildNetwork( trndata.indim, 5, trndata.outdim, outclass=SoftmaxLayer )
trainer = BackpropTrainer( fnn, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.01)

ticks = arange(-3.,6.,0.2)
X, Y = meshgrid(ticks, ticks)
# need column vectors in dataset, not arrays
griddata = ClassificationDataSet(2,1, nb_classes=3)
for i in xrange(X.size):
    griddata.addSample([X.ravel()[i],Y.ravel()[i]], [0])
griddata._convertToOneOfMany()  # this is still needed to make the fnn feel comfy

for i in range(2):
    trainer.trainEpochs( 1 )

for i in xrange(0,len(tstdata)):

    a=int(tstdata['target'][i][0])
    b=int(tstdata['target'][i][1])
    c=int(tstdata['target'][i][2])
    
    res=-1
    if (a==1):
        res+=1
    elif (b==1):
        res+=2
    elif (c==1):
        res+=3

    if ( res!= tstdata['class'][i] ):
        print("Exemplo - ", i)
        print ("classe: {}".format(res) )
        print ("saida:  {}".format(int(tstdata['class'][i])) ) 
        print ("--------------" )

    '''
    trnresult = percentError( trainer.testOnClassData(),trndata['class'] )
    tstresult = percentError( trainer.testOnClassData(dataset=tstdata ), tstdata['class'] )

    print "epoch: %4d" % trainer.totalepochs, \
          "  train eerror: %5.2f%%" % trnresult, \
          "  test error: %5.2f%%" % tstresult
    




    trnresult = percentError( trainer.testOnClassData(),
                              trndata['class'] )
    tstresult = percentError( trainer.testOnClassData(
           dataset=tstdata ), tstdata['class'] )

    print "epoch: %4d" % trainer.totalepochs, \
          "  train error: %5.2f%%" % trnresult, \
          "  test error: %5.2f%%" % tstresult
    
    '''

    '''
    figure(1)
    ioff()  # interactive graphics off
    clf()   # clear the plot
    hold(True) # overplot on
    for c in [0,1,2]:
        here, _ = where(tstdata['class']==c)
        plot(tstdata['input'][here,0],tstdata['input'][here,1],'o')
    if out.max()!=out.min():  # safety check against flat field
        contourf(X, Y, out)   # plot the contour
    ion()   # interactive graphics on
    draw()  # update the plot
    ioff()
    show()
    '''