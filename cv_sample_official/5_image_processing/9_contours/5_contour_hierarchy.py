# There is no code in this section

#
# In the function cv2.findContours(), we can pass 4 different retrieval mode, they are:
# 1. RETR_LIST
# 2. RETR_EXTERNAL
# 3. RETR_CCOMP
# 4. RETR_TREE
#
# and a "hierarchy" return value, which has the sequence of:
# [Next, Previous, First_Child, Parent]
#
#
#
# 1. RETR_LIST: no hierarchy, no parent, no child
# 2. RETR_EXTERNAL: only the parents(outest) contours are returned
# 3. RETR_CCOMP: 2-level hierarchy, externals contour and inside hole contour
# 4. RETR_TREE: full hierarchy
#
#
# Next: the next contour in the SAME hierarchy
# Previous: the previous contour in the SAME hierarchy
# First_Child: the direct first child of this contour
# Parent: the parent
