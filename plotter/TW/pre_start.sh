# NOTE: these commands are EQUIVALENT to the definition of the alias "root6".
# It is compulsory to explicit them as employing the queue service the aliases
# are not propagated. In the case of a modification of the alias, these 
# instructions must be updated as well.

# The alias is also included, as sometimes the following executions, mysteriously,
# do not work (but the alias yes). This, as a consequence of the previous
# paragraph, will only serve as by-pass when executing the code directly, but not
# when sending it as a job.

root6

source /cms/slc6_amd64_gcc530/external/gcc/5.3.0/etc/profile.d/init.sh
source /cms/slc6_amd64_gcc530/external/python/2.7.11-giojec2/etc/profile.d/init.sh
source /cms/slc6_amd64_gcc530/external/python/2.7.11-giojec2/etc/profile.d/dependencies-setup.sh
source /cms/slc6_amd64_gcc530/external/cmake/3.5.2/etc/profile.d/init.sh
source /opt/root6/bin/thisroot.sh

source /opt/PAF/PAF_setup.sh
