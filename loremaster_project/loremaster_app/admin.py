from django.contrib import admin

from loremaster_app.models import Ability, Spell, Skill, CombatSkill, SpecialAbility, Material, Treasure, Monster

# Register your models here.
admin.site.register(Ability)
admin.site.register(Spell)
admin.site.register(Skill)
admin.site.register(CombatSkill)
admin.site.register(SpecialAbility)
admin.site.register(Material)
admin.site.register(Treasure)
admin.site.register(Monster)