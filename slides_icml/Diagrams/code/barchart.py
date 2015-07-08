import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# plt.rc('text', usetex=True)
plt.rc('font', size=14)
matplotlib.rc('pdf', fonttype=42)

algname=sys.argv[1]  #"PEGASOS"
if algname =="A1-noisefree":
    alg_xlim=[0,3]
    alg_ylim=[0,2]

    file_accuracy="../Accuracy-"+algname+".csv"
    file_std = "../Accuracy-"+algname+"-stds.csv"
    legend_labels = ["FastICA" , "HKICA" , "FPCA" ,  "DICA", "MDICA"]
    group_labels = [r" "]

    accuracy_vals = np.genfromtxt(file_accuracy, delimiter=",")
    std_vals = np.genfromtxt(file_std, delimiter=",")



    N=1  #number of k-CV groups (5,10,100,LOOCV)

    ind = np.arange(N)*4  # the x locations for the groups
    width = 0.40       # the width of the bars
    half_width = 0.15

    fig, ax = plt.subplots()


    ax.bar(ind, 
           accuracy_vals[0] , width, color='c', yerr=std_vals[0], linewidth=1.5, error_kw={'linewidth': 3, 'mew':3, 'sm':3})

    ax.bar(ind+width+half_width, 
           accuracy_vals[1] , width, color='r', yerr=std_vals[1], linewidth=1.5, error_kw={'linewidth': 3, 'mew':3, 'sm':3})

    ax.bar(ind+2*width+2*half_width, 
           accuracy_vals[2] , width, color='b', yerr=std_vals[2], linewidth=1.5, error_kw={'linewidth': 3, 'mew':3, 'sm':3})

    ax.bar(ind+3*width+3*half_width, 
           accuracy_vals[3] , width, color='y', yerr=std_vals[3], linewidth=1.5, error_kw={'linewidth': 3, 'mew':3, 'sm':3})

    ax.bar(ind+4*width+4*half_width, 
           accuracy_vals[4] , width, color='g', yerr=std_vals[4], linewidth=1.5, error_kw={'linewidth': 3, 'mew':3, 'sm':3})


    # add some text for labels, title and axes ticks
    ax.set_ylabel('Reconstruction errors')
    ax.set_title('Reconstruction errors: mixing matrix: A1.')
    ax.set_xticks(ind+2*width+half_width)
    ax.set_xticklabels( group_labels )
    ax.set_ylim(alg_ylim)
    ax.set_xlim(alg_xlim)


    ax.legend( legend_labels , loc='upper center', bbox_to_anchor=(0.5, 1.01),
              ncol=2, fancybox=True, shadow=True)

    fig.savefig("../barchart-"+algname+".pdf", format="PDF")

elif algname=="A1vsA4-noisy": 
    # A1 vs A4; noise 0.4;
    alg_xlim=[0,7]
    alg_ylim=[0,3]

    file_accuracy="../Accuracy-"+algname+".csv"
    file_std = "../Accuracy-"+algname+"-stds.csv"
    legend_labels = ["FastICA" , "HKICA" , "FPCA" ,  "DICA", "MDICA"]
    group_labels = [r"Matrix: A1", r"Matrix: A4"]

    accuracy_vals = np.genfromtxt(file_accuracy, delimiter=",")
    std_vals = np.genfromtxt(file_std, delimiter=",")



    N=2  #number of k-CV groups (5,10,100,LOOCV)

    ind = np.arange(N)*4  # the x locations for the groups
    width = 0.40       # the width of the bars
    half_width = 0.15

    fig, ax = plt.subplots()


    ax.bar(ind, 
           accuracy_vals[:,0] , width, color='c', yerr=std_vals[:,0], linewidth=1.5, error_kw={'linewidth': 3, 'mew':3, 'sm':3})

    ax.bar(ind+width+half_width, 
           accuracy_vals[:,1] , width, color='r', yerr=std_vals[:,1], linewidth=1.5, error_kw={'linewidth': 3, 'mew':3, 'sm':3})

    ax.bar(ind+2*width+2*half_width, 
           accuracy_vals[:,2] , width, color='b', yerr=std_vals[:,2], linewidth=1.5, error_kw={'linewidth': 3, 'mew':3, 'sm':3})

    ax.bar(ind+3*width+3*half_width, 
           accuracy_vals[:,3] , width, color='y', yerr=std_vals[:,3], linewidth=1.5, error_kw={'linewidth': 3, 'mew':3, 'sm':3})

    ax.bar(ind+4*width+4*half_width, 
           accuracy_vals[:,4] , width, color='g', yerr=std_vals[:,4], linewidth=1.5, error_kw={'linewidth': 3, 'mew':3, 'sm':3})


    # add some text for labels, title and axes ticks
    ax.set_ylabel('Reconstruction errors')
    ax.set_title('Reconstruction errors for different mixing matrices')
    ax.set_xticks(ind+2*width+half_width)
    ax.set_xticklabels( group_labels )
    ax.set_ylim(alg_ylim)
    ax.set_xlim(alg_xlim)


    ax.legend( legend_labels , loc='upper center', bbox_to_anchor=(0.5, 1.01),
              ncol=2, fancybox=True, shadow=True)

    fig.savefig("../barchart-"+algname+".pdf", format="PDF")
    
elif algname=="recursive-noisy": 
    # A1 vs A4; noise 0.4;
    alg_xlim=[0,8]
    alg_ylim=[0,2.5]

    file_accuracy="../Accuracy-"+algname+".csv"
    file_std = "../Accuracy-"+algname+"-stds.csv"
    legend_labels = ["HKICA" , "DICA", "MDICA"]
    group_labels = [r"A1", r"A1 Recursive", r"A4", r"A4 Recursive"]

    accuracy_vals = np.genfromtxt(file_accuracy, delimiter=",")
    std_vals = np.genfromtxt(file_std, delimiter=",")



    N=4  #number of k-CV groups (5,10,100,LOOCV)

    ind = np.arange(N)*2  # the x locations for the groups
    width = 0.40       # the width of the bars
    half_width = 0.15

    fig, ax = plt.subplots()


    ax.bar(ind, 
           accuracy_vals[:,0] , width, color='c', yerr=std_vals[:,0], linewidth=1.5, error_kw={'linewidth': 3, 'mew':3, 'sm':3})

    ax.bar(ind+width+half_width, 
           accuracy_vals[:,1] , width, color='r', yerr=std_vals[:,1], linewidth=1.5, error_kw={'linewidth': 3, 'mew':3, 'sm':3})

    ax.bar(ind+2*width+2*half_width, 
           accuracy_vals[:,2] , width, color='b', yerr=std_vals[:,2], linewidth=1.5, error_kw={'linewidth': 3, 'mew':3, 'sm':3})



    # add some text for labels, title and axes ticks
    ax.set_ylabel('Reconstruction errors')
    ax.set_title(' ')
    ax.set_xticks(ind+2*width+half_width)
    ax.set_xticklabels( group_labels )
    ax.set_ylim(alg_ylim)
    ax.set_xlim(alg_xlim)


    ax.legend( legend_labels , loc='upper center', bbox_to_anchor=(0.5, 1.01),
              ncol=2, fancybox=True, shadow=True)

    fig.savefig("../barchart-"+algname+".pdf", format="PDF")

else:
    print "BAD ALG NAME!"
    exit(0)