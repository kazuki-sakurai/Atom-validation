#!usr/bin/env python

class tex_format:
    begin_document = '''
        \\documentclass[12pt]{article}

        \\setlength\\topmargin{0mm}
        \\setlength\\headheight{0mm}
        \\setlength\\headsep{0mm} 
        \\setlength\\oddsidemargin{0mm}
        \\setlength\\evensidemargin{0mm}
        \\setlength\\textwidth{165mm}
        \\setlength\\textheight{220mm}    

        \\usepackage{fancyvrb}
        \\usepackage{amssymb}
        \\usepackage{amsmath}
        \\usepackage{enumerate}
        \\usepackage{slashed}
        \\usepackage{graphicx}
        \\usepackage{color}
        \\usepackage[tight]{subfigure}
        \\usepackage{float}
        \\usepackage{ulem}
        \\usepackage{url}
        \\usepackage{colortbl}
        
        \\begin{document}
    '''
    end_document = '''        
        \\end{document}
    '''

def rout(val, n):
    try:
        return '$ '+ str(round(val, n)) +' $'
    except:
        return val

def make_table(ananame, vname, table_caption, 
               texname_list, eff_exp, err_exp, eff_atom, err_atom, ratio_eff, ratio_eff_sig, 
               i_denom, Reff_exp, Rerr_exp, Reff_atom, Rerr_atom, ratio_R, ratio_R_sig):
    
    err_exp[0] = ' '
    err_atom[0] = ' '
    table_lists = []
    for i in range(len(texname_list)):
        pm = ' '         
        if i > 0: pm = ' $\\pm$ '
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

    return table_writer(table_lists, vname, table_caption, ratio_eff, ratio_eff_sig, ratio_R, ratio_R_sig)


def table_writer(table_lists_orig, vname, table_caption, ratio_eff, ratio_eff_sig, ratio_R, ratio_R_sig):

    table_lists = []
    for i in range(len(table_lists_orig)):

        line_list = table_lists_orig[i]
        try:
            eff = ratio_eff[i]
            eff_sig = ratio_eff_sig[i]
            Rval = ratio_R[i]
            Rsig = ratio_R_sig[i]
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
        
    #################################################

    dsla = '\\' + '\\'

    texlines = []

    texlines.append('\\renewcommand{\\arraystretch}{1.3}')
    texlines.append('\\begin{table}[h!]')
    texlines.append('\\begin{center}')
    texlines.append('\\scalebox{0.65}[0.75]{ ')

    texlines.append('\\begin{tabular}{c|l||c|c|>{\columncolor{yellow}}c|c||c|c|c|>{\columncolor{yellow}}c|c}')
    texlines.append('\\hline')
    texlines.append( headline[:-2] + dsla )
    texlines.append('\\hline')
    for line in table_lines: texlines.append( line[:-2] + dsla )
    texlines.append('\\hline')

    texlines.append('\\end{tabular}')
    texlines.append('}')
    texlines.append('\\caption{\\small ' + table_caption + '}') 
    texlines.append('\\label{tab:cflow_' + vname + '}')
    texlines.append('\\end{center}')
    texlines.append('\\label{default}')
    texlines.append('\\end{table}')

    #for t in texlines: print t
    return texlines



