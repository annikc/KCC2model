import struct
import numpy as np
import matplotlib.pyplot as plt


def plot_Ka(cal):
	V_ak = 390 #/s from Kohout 2002
	h_k = 1.5 # from Kohout 2002
	R_k = 2.37e-6 #M from Kohout 2002
	v_ik = 32.1 #/s from Kohout 2002
	v_ak = (V_ak*(cal)**h_k)/(R_k**h_k + (cal)**h_k)
	K_i = v_ik/(v_ak + v_ik)
	K_a = v_ak/(v_ak + v_ik)
	return K_a	

def plot_Pa(cal):
	V_ap = 100 #200 # /M*s
	h_p = 3 #(2.8-3 from Stemmer & Klee 1994)
	R_p = 7.943e-7 #M
	v_ip = 10 #/s from Quintana, Waxham 2005
	v_ap = (V_ap*(cal)**h_p)/(R_p**h_p + (cal)**h_p)
	P_i = v_ip/(v_ap + v_ip)
	P_a = v_ap/(v_ap + v_ip)

	return P_a
	
rec_cal = np.zeros(100000)
rec_cal2 = np.linspace(0, 3.5e-6, 10000)
rec_Ka = np.zeros(len(rec_cal2))
rec_Pa = np.zeros(len(rec_cal2))
resting_ca = 100e-9


for i in range(len(rec_cal2)):
	rec_Ka[i] = plot_Ka(rec_cal2[i])
	rec_Pa[i] = plot_Pa(rec_cal2[i])








#def save(path, ext='png', close=True, verbose=True):
#    """Save a figure from pyplot.
#
#    Parameters
#    ----------
#    path : string
#        The path (and filename, without the extension) to save the
#        figure to.
#
#    ext : string (default='png')
#        The file extension. This must be supported by the active
#        matplotlib backend (see matplotlib.backends module).  Most
#        backends support 'png', 'pdf', 'ps', 'eps', and 'svg'.
#
#    close : boolean (default=True)
#        Whether to close the figure after saving.  If you want to save
#        the figure multiple times (e.g., to multiple formats), you
#        should NOT close it in between saves or you will have to
#        re-plot it.
#
#    verbose : boolean (default=True)
#        Whether to print information about when and where the image
#        has been saved.
#
#    """
#    
#    # Extract the directory and filename from the given path
#    directory = os.path.split(path)[0]
#    filename = "%s.%s" % (os.path.split(path)[1], ext)
#    if directory == '':
#        directory = '.'
# 
#    # If the directory does not exist, create it
#    if not os.path.exists(directory):
#        os.makedirs(directory)
# 
#    # The final path to save to
#    savepath = os.path.join(directory, filename)
# 
#    if verbose:
#        print("Saving figure to '%s'..." % savepath),
# 
#    # Actually save the figure
#    plt.savefig(savepath)
#    
#    # Close it
#    if close:
#        plt.close()
# 
#    if verbose:
#        print("Done")

plt.plot(rec_cal2, rec_Ka, 'b', label='Active Kinase')
plt.plot(rec_cal2, rec_Pa, 'r', label='Active Phosphatase')
plt.legend(loc=4)
plt.xlabel('Calcium Concentration (M)')
plt.ylabel('Proportion of Enzyme in Active State')
#plt.xlim([0, 0.000003])
plt.annotate('Resting Ca$^{2+}$', xy=(resting_ca, 0), xytext=(0.000001, 0.2),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
#save("../Thesis/fig/PaKa", ext="png", close=True, verbose=True)

plt.savefig('kapa.png', format='png')
