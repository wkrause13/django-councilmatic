from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import strip_entities, strip_tags
import re

register = template.Library()

@register.filter
@stringfilter
def sentence_case(value):
    return value.replace("_", " ").capitalize()

@register.filter
@stringfilter
def inferred_status_label(status):
    return "<span class='label label-"+status.lower()+"'>"+status+"</span>"

@register.filter
@stringfilter
def facet_name(value):
    if value == 'bill_type': return 'Legislation type'
    if value == 'sponsorships': return 'Sponsor'
    if value == 'controlling_body': return 'Controlling body'
    if value == 'inferred_status': return 'Legislation status'

@register.filter
@stringfilter
def remove_action_subj(bill_action_desc):
    # removes 'by X' from bill action descriptions & expands abbrevs
    # for more readable action labels
    clean_action = re.sub(r'\bComm\b', 'Committee', bill_action_desc)
    clean_action = re.sub(r'\bRecved\b', 'Received', clean_action)
    clean_action = re.sub(r'[,\s]*by\s[^\s]*', '', clean_action)

    # shorten the really long action descriptions for approval w/ modifications
    if 'approved with modifications' in clean_action.lower():
        clean_action = 'Approved with Modifications'

    return clean_action

@register.filter
@stringfilter
def short_blurb(text_blob):
    if len(text_blob) > 196:
        blurb = text_blob[:196]
        blurb = blurb[:blurb.rfind(' ')]+' ...'
        return blurb
    else:
        return text_blob

@register.filter
@stringfilter
def short_title(text_blob):
    if len(text_blob) > 28:
        blurb = text_blob[:24]
        blurb = blurb[:blurb.rfind(' ')]+' ...'
        return blurb
    else:
        return text_blob

@register.filter
@stringfilter
def strip_mailto(email):
    return re.sub('mailto:', '', email)

@register.filter
@stringfilter
def committee_topic_only(committee_name):
    clean = re.sub('Committee on', '', committee_name)
    clean = re.sub('Subcommittee on', '', clean)
    if 'Mental Health, Developmental Disability' in clean:
        clean = 'Mental Health & Disability'
    return clean

@register.filter
@stringfilter
def clean_html(text):
    return strip_entities(strip_tags(text)).replace('\n','')

@register.filter
@stringfilter
def alternative_identifiers(id_original):
    id_1 = re.sub(" ", " 0", id_original)
    id_2 = re.sub(" ", "", id_original)
    id_3 = re.sub(" ", "", id_1)
    return id_original+' '+id_1+' '+id_2+' '+id_3

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def format_date_sort(s, fmt='%Y%m%d%H%M'):
    if s:
        return s.strftime(fmt)
    else:
        return '0'
