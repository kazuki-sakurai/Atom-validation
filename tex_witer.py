#!usr/bin/env python


def rout(val, n):
    try:
        return str(round(val, n))
    except:
        return val

def make_table(ananame, vname, table_name, description, table_caption, 
               texname_list, eff_exp, err_exp, eff_atom, err_atom, ratio_eff, ratio_eff_sig, 
               i_denom, Reff_exp, Rerr_exp, Reff_atom, Rerr_atom, ratio_R, ratio_R_sig):
    
    table_lists = []
    pm = ' $\\pm$ '
    for i in range(len(texname_list)):
        line_list = []
        line_list.append(str(i))    # 1
        line_list.append(str(texname_list[i]))  # 2 
        line_list.append( rout(eff_exp[i], 2) + pm + rout(err_exp[i], 2) )  # 3
        line_list.append( rout(eff_atom[i], 2) + pm + rout(err_atom[i], 2) )  # 4
        line_list.append( rout(ratio_eff[i], 2) ) # 5
        line_list.append( rout(ratio_eff_sig[i], 2) ) # 6

        line_list.append(str(i_denom[i])) # 7
        line_list.append( rout(Reff_exp[i], 2) + pm + rout(Rerr_exp[i], 2) )  # 8
        line_list.append( rout(Reff_atom[i], 2) + pm + rout(Rerr_atom[i], 2) )  # 9
        line_list.append(rout(ratio_R[i], 2)) # 10
        line_list.append(rout(ratio_R_sig[i], 2)) # 11

        table_lists.append(line_list)

    texlines = []

    texlines.append('\\documentclass[12pt]{article}')

    texlines.append('\\setlength\\topmargin{0mm}')
    texlines.append('\\setlength\headheight{0mm}')
    texlines.append('\\setlength\headsep{0mm}') 
    texlines.append('\\setlength\oddsidemargin{0mm}')
    texlines.append('\\setlength\evensidemargin{0mm}')
    texlines.append('\\setlength\\textwidth{165mm}')
    texlines.append('\\setlength\\textheight{220mm}')    

    texlines.append('\\usepackage{fancyvrb}')
    texlines.append('\\usepackage{amssymb}')
    texlines.append('\\usepackage{amsmath}')
    texlines.append('\\usepackage{enumerate}')
    texlines.append('\\usepackage{slashed}')
    texlines.append('\\usepackage{graphicx}')
    texlines.append('\\usepackage{color}')
    texlines.append('\\usepackage[tight]{subfigure}')
    texlines.append('\\usepackage{float}')
    texlines.append('\\usepackage{ulem}')
    texlines.append('\\usepackage{url}')
    texlines.append('\\usepackage{colortbl}')
    texlines.append('')
    texlines.append('')
    texlines.append('\\begin{document}')
    texlines.append('')
    texlines.append('\\subsection*{ ' + table_name + ' }')
    texlines.append('')
    texlines.append(description)
    texlines.append('')
    texlines.append('')

    texlines += table_writer(table_lists, vname, table_caption)

    texlines.append('')
    texlines.append('')    
    texlines.append('\\end{document}')

    return texlines


def table_writer(table_lists_orig, vname, table_caption):

    table_lists = []
    for line_list in table_lists_orig:

        try:
            eff = float(line_list[4])
            eff_sig = float(line_list[5]) 
            Rval = float(line_list[9])
            Rsig = float(line_list[10])
            warn = 0    
            if abs(1. - eff) > 0.300000001:
                if abs(eff_sig) > 4.00000001:
                    #warn = 2
                    line_list[4] = '\\color{red}\\bf ' + line_list[4]
                else:
                    #warn = 1
                    line_list[4] = '\\color{blue}\\bf ' + line_list[4]        
            if abs(1. - Rval) > 0.300000001:
                if abs(Rsig) > 4.00000001:
                    warn = 2
                    line_list[9] = '\\color{red}\\bf ' + line_list[9]                
                else:
                    if warn <= 1: warn = 1
                    line_list[9] = '\\color{blue}\\bf ' + line_list[9]

            if warn == 1:
                line_list[1] = '\\cellcolor{cyan} ' + line_list[1]
            if warn == 2:
                line_list[1] = '\\cellcolor{magenta} ' + line_list[1]
        except: pass
        table_lists.append(line_list)        

    table_lines = []
    for line_list in table_lists:
        line = ''
        for elem in line_list: line += elem + ' & '
        table_lines.append(line)

    #######################################

    header = ['\\#', 'cut name', '$\\epsilon_{\\rm Exp}$', '$\\epsilon_{\\rm Atom}$', 
              '$\\frac{\\rm Atom}{\\rm Exp}$', 
              '$\\frac{({\\rm Exp} - {\\rm Atom})}{\\rm Error}$',
              '$\\#/?$',  
              '$R_{\\rm Exp}$', '$R_{\\rm Atom}$', 
              '$\\frac{\\rm Atom}{\\rm Exp}$', 
              '$\\frac{({\\rm Exp} - {\\rm Atom})}{\\rm Error}$'
              ]

    headline = ''
    for elem in header: headline += elem + ' & '

    print 'head line = ', len(header)
    print 'tab line = ', len(table_lists[0])
        
    #################################################

    dsla = '\\' + '\\'

    texlines = []

    texlines.append('\\renewcommand{\\arraystretch}{1.3}')
    texlines.append('\\begin{table}[h!]')
    texlines.append('\\begin{center}')
    texlines.append('\\scalebox{0.7}[0.8]{ ')

    texlines.append('\\begin{tabular}{c|c||c|c|>{\columncolor{yellow}}c|c||c|c|c|>{\columncolor{yellow}}c|c}')
    texlines.append('\\hline')
    texlines.append( headline[:-2] + dsla )
    texlines.append('\\hline')
    for line in table_lines: texlines.append( line[:-2] + dsla )
    texlines.append('\\hline')

    texlines.append('\\end{tabular}')
    texlines.append('}')
    texlines.append('\\caption{' + table_caption + '}') 
    texlines.append('\\label{tab:cflow_' + vname + '}')
    texlines.append('\\end{center}')
    texlines.append('\\label{default}')
    texlines.append('\\end{table}')

    #for t in texlines: print t
    return texlines



