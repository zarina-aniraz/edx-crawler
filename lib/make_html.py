#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import codecs
from bs4 import BeautifulSoup 



def extract_unit_html(subsection_page):
    unit = []
    #for e_html in subsection_page:
    tmp=[]
    idx = 0
    while tmp is not None:
      id_name = "seq_contents_"+str(idx)
      tmp = subsection_page.find("div", {"id": id_name})
      unit.append(tmp)
      idx = idx + 1 
    unit.remove(None)
    print str(idx-1)
    return unit

def save_html_to_file(args, selections, all_urls, headers):
    """
    Save html to file. Filename is specified by the user. this function
    is to save html of each subsection for further analysis purpors
    """

    sub_idx = 0
    for selected_course, selected_sections in selections.items():
        coursename = directory_name(selected_course.name)
        
        for selected_section in selected_sections:
            section_dirname = "%02d-%s" % (selected_section.position,
                                           selected_section.name)
            target_dir = os.path.join(args.html_dir, coursename,
                                      clean_filename(section_dirname))
            mkdir_p(target_dir)
            
            for subsection in selected_section.subsections:
               
                #for url in all_urls:
                #if type(subsection.name) == None:
                print subsection.name
                if subsection.name == None:
                    subsection.name = 'Untitled'
                target_subdir = os.path.join(target_dir, clean_filename(subsection.name))
                mkdir_p(target_subdir)
                logging.info('url: '+ str(all_urls[sub_idx]) + ', subsection: ' + str(subsection.name))
                page = get_page_contents(str(all_urls[sub_idx]), headers)
                page = string.replace(page, '&lt;', '<')
                page = string.replace(page, '&gt;', '>')
                page = string.replace(page, '&#34;', '"')
                page = string.replace(page, 'nbsp;', ' ')
                #page = string.replace(page, '&amp;', '&')
                soup = BeautifulSoup(page)
                units = extract_unit_html(soup)
                counter = 0
                sub_idx = sub_idx+1
                for unit in units:
                    
                    filename_template = "seq_contents_"+str(counter) +".html"
                    filename = os.path.join(target_subdir, filename_template)
                    logging.info('path: '+ str(target_subdir) + ', filename: ' + str(filename))
                    file_ = sys.stdout if filename == '-' else codecs.open( filename, 'w', 'utf-8')
                    file_.writelines(unit.prettify())
                    file_.close()
                    counter += 1

                  
