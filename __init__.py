# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

from yummly import Client

import time

__author__ = 'ajwkc'

LOGGER = getLogger(__name__)

# Preps the Yummly API ID and key
client = Client(api_id="578ccc53", api_key="1d102bfd626c6a634b477219350a6233", timeout=5.0, retries=0)


class RecipeSkill(MycroftSkill):

    def __init__(self):
        super(RecipeSkill, self).__init__(name="RecipeSkill")

        # Listens for "how do I cook ____________"

    @intent_handler(IntentBuilder("RecipeIntent").require("Query").require("Cook").require("Food"))
    def handle_recipe_intent(self, message):
        # Searches for "Food" and grabs the first result
        food = message.data.['Food']
        search = client.search(food)
        match = search.matches[0]
        recipe = client.recipe(match.id)

        # Reads the ingredients
        self.speak_dialog("Read")
        for ingredient in recipe.ingredientLines:
            self.speak(ingredient)
            time.sleep(1)

    def stop(self):
        pass


def create_skill():
    return RecipeSkill()
