#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
Listening Experiment Py: SAQI - A Spatial Audio Inventory

        (C) 2021 by Tim Lübeck
                TH Köln - University of Applied Sciences
                Institute of Communications Engineering
                Department of Acoustics and Audio Signal Processing
"""

from .SAQI_definitions import Item, attribute_names_en, attribute_names_ger, circumscriptions_en, circumscriptions_ger, \
                             labels_en, labels_ger, phrases_en, phrases_ger

class Attribute():
    def __init__(self, category, item, phrase=None, rating_scale_mode='bipolar'):
        if phrase is None:
            phrase = [phrases_en[1], phrases_ger[1]]
        self.id = item.value
        self.quality = [attribute_names_en[item.value], attribute_names_ger[item.value]]
        self.category = category
        self.scale_end_label_low = [labels_en[item.value][0], labels_ger[item.value][0]]
        self.scale_end_label_high = [labels_en[item.value][1], labels_ger[item.value][1]]
        self.circumscription = circumscriptions_en[item.value], circumscriptions_ger[item.value]
        self.phrase = phrase
        self.rating_scale_mode = rating_scale_mode  #  according to lindau15 just overall difference and sequence of events are unipolar scales
                                                    #  however, some ecustom attributes require unipolar scales
        self.language = 'english'
        self.set_language('english')

    def set_language(self, language):
        self.language = language
        if self.language == 'english':
            self.language_id = 0
        elif self.language == 'german':
            self.language_id = 1

    def get_category_name(self):
        return self.category[self.language_id]

    def get_quality_name(self):
        return self.quality[self.language_id]

    def get_scale_end_label_low(self):
        return self.scale_end_label_low[self.language_id]

    def get_scale_end_label_high(self):
        return self.scale_end_label_high[self.language_id]

    def get_circumscription(self):
        return self.circumscription[self.language_id]

    def get_phrase(self):
        return self.phrase[self.language_id]


class Category:
    def __init__(self):
        self.name = ['', '']
        self.id = 0
        self.language = 'english'

    def get_name(self):
        if self.language == 'english':
            return self.name[0]
        elif self.language == 'german':
            return self.name[1]


# NOTES: In original SAQI manual the following is proposed:
# * horizontal and vertical scale allows to type direction in degree directly + radio button vor clock and counterclockwise!
# * front back position to radio buttons 'not confused' 'confused' (dichotomous scale)
# * maximum 9 sliders per 'SIDE'
# * each stimuli has be listen to at least one time -- > whisper: just for the overall difference quality WHY?!
# * randomize assignment A and B

# ----------------------------------------------------------------------------
class OveralDifference(Attribute):

    def __init__(self):
        super().__init__(category='', item=Item.difference, phrase=[phrases_en[0], phrases_ger[0]])
        self.rating_scale_mode = 'unipolar'

class Timbre(Category):

    def __init__(self):
        super().__init__()
        self.name = ['Timbre', 'Klangfarbe']
        self.id = 1
        self.ToneColorBrightDark = Attribute(self.name, Item.toneColorBrightDark)
        self.HighFrequencyToneColor = Attribute(self.name, Item.highFrequencyToneColor)
        self.MidFrequencyToneColor = Attribute(self.name, Item.midFrequencyToneColor)
        self.lowFrequencyToneColor = Attribute(self.name, Item.lowFrequencyToneColor)
        self.sharpness = Attribute(self.name, Item.sharpness)
        self.roughness = Attribute(self.name, Item.roughness)
        self.combFilterColoration = Attribute(self.name, Item.combFilterColoration)
        self.metallicToneColor = Attribute(self.name, Item.metallicToneColor)

        # custom attributes:
        self.coloration = Attribute(self.name, Item.coloration, rating_scale_mode='unipolar')

class Tonalness(Category):

    def __init__(self):
        super().__init__()
        self.name = ['Tonalness', 'Tonalität']
        self.id = 2
        self.Tonalness = Attribute(self.name, Item.tonalness)
        self.Pitch = Attribute(self.name, Item.pitch)
        self.DopplerEffect = Attribute(self.name, Item.dopplerEffect)


class Geometry(Category):

    def __init__(self):
        super().__init__()
        self.name = ['Geometry', 'Geometrie']
        self.id = 3
        self.HorizontalDirection = Attribute(self.name, Item.horizontalDirection)
        self.VerticalDirection = Attribute(self.name, Item.verticalDirection)
        self.externalization = Attribute(self.name, Item.externalization)

        # custom attributes
        self.sourcePosition = Attribute(self.name, Item.sourcePosition, rating_scale_mode='unipolar')
        self.sourceWidth = Attribute(self.name, Item.sourceWidth)

class Room(Category):

    def __init__(self):
        super().__init__()
        self.name = ['Room', 'Raum']
        self.id = 4
        self.durationOfReverberation = Attribute(self.name, Item.durationOfReverberation)
        self.envelopment = Attribute(self.name, Item.envelopment)

class TimeBehaviour(Category):

    def __init__(self):
        super().__init__()
        self.name = ['Time Behaviour', 'Zeitverhalten']
        self.id = 5

class Dynamics(Category):

    def __init__(self):
        super().__init__()
        self.name = ['Dynamics', 'Dynamik']
        self.id = 6

class Artifacts(Category):

    def __init__(self):
        super().__init__()
        self.name = ['Artifacts', 'Artefakte']
        self.id = 7

class General(Category):

    def __init__(self):
        super().__init__()
        self.name = ['General', 'Allgemeines']
        self.id = 8
        self.Clarity = Attribute(self.name, Item.clarity)
        
