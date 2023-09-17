from django.db import models


# Defines table Ability for many-to-many relationshop to Monster
class Ability(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    level = models.IntegerField()

    def __str__(self):
        return self.name


# Defines table Spell for many-to-many relationshop to Monster
class Spell(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    level = models.IntegerField()

    def __str__(self):
        return self.name


# Defines table Skill for many-to-many relationshop to Monster
class Skill(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    level = models.IntegerField()
    specialization = models.BooleanField()

    def __str__(self):
        return self.name


# Defines table CombatSkill for many-to-many relationshop to Monster
class CombatSkill(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    level = models.IntegerField()
    specialization = models.BooleanField()

    def __str__(self):
        return self.name


# Defines SpecialAbility for many-to-many relationshop to Monster
class SpecialAbility(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    level = models.IntegerField()

    def __str__(self):
        return self.name


# Defines Material for many-to-many relationshop to Monster
class Material(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


# Defines Treasure for many-to-many relationshop to Monster
class Treasure(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


# Monster model, does not include derivitive stats such as AC
class Monster(models.Model):

    # descriptive stats
    name = models.CharField(max_length=200)
    description = models.TextField()
    species = models.CharField(max_length=200)
    size = models.CharField(max_length=100)
    environment = models.CharField(max_length=200)
    # if it's a probability (0-1), otherwise use IntegerField
    chance_to_appear = models.FloatField()
    tameable = models.BooleanField()
    befriendable = models.BooleanField()

    # attributes
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    agility = models.IntegerField()
    constitution = models.IntegerField()
    endurance = models.IntegerField()
    stamina = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    insight = models.IntegerField()
    willpower = models.IntegerField()
    charisma = models.IntegerField()
    persuasion = models.IntegerField()
    luck = models.IntegerField()
    perception = models.IntegerField()

    # many-to-many relationships
    abilities = models.ManyToManyField(Ability)
    spells = models.ManyToManyField(Spell)
    skills = models.ManyToManyField(Skill)
    combat_skills = models.ManyToManyField(CombatSkill)
    special_abilities = models.ManyToManyField(SpecialAbility)
    harvested_materials = models.ManyToManyField(Material)
    treasure = models.ManyToManyField(Treasure)

    def __str__(self):
        return self.name
