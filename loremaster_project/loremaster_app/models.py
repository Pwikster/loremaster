from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class BaseAbility(models.Model):
    """Base model for abilities, spells, skills, and special abilities."""

    name = models.CharField(max_length=200)
    description = models.TextField()
    level = models.PositiveIntegerField()
    racial_ability = models.BooleanField(default=False)
    racial_level = models.PositiveIntegerField(null=True, blank=True)
    is_maneuver = models.BooleanField(default=False)
    is_flaw = models.BooleanField(default=False)
    is_talent = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ImmunityOrResistanceOrWeak(models.Model):
    """Model for immunities or resistances."""

    element = models.CharField(max_length=200)
    resistant_or_weak_level = models.IntegerField()
    is_immune = models.BooleanField(default=False)
    racial_ability = models.BooleanField(default=False)
    racial_level = models.PositiveIntegerField(null=True, blank=True)
    is_maneuver = models.BooleanField(default=False)
    is_flaw = models.BooleanField(default=False)
    is_talent = models.BooleanField(default=False)

    def __str__(self):
        return self.element


# Defines table Ability for many-to-many relationshop to Monster
class Ability(BaseAbility):
    """Model for abilities."""

    pass

class Material(models.Model):
    """Model for materials."""
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

# Defines table Spell for many-to-many relationshop to Monster
class Spell(BaseAbility):
    """Model for spells."""

    COST_CHOICES = (
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    )

    CASTING_TYPE_CHOICES = (
        ("damage", "Damage"),
        ("healing", "Healing"),
        ("buff", "Buff"),
        ("debuff", "Debuff"),
        ("other", "Other"),
    )

    SCHOOL_CHOICES = (
        ("arcane", "Arcane"),
        # Add other schools as needed
    )

    CATEGORY_CHOICES = (
        ("offensive_arcane", "Offensive Arcane (Component Based)"),
        ("buff", "Buff"),
        ("debuff", "Debuff"),
        # Add other categories as needed
    )

    cost = models.CharField(max_length=50, choices=COST_CHOICES, null=True)
    components = models.TextField(
        help_text="List of components required for the spell.", null=True
    )
    materials = models.ManyToManyField(Material, blank=True)
    range = models.CharField(max_length=200, null=True)
    casting_time = models.CharField(max_length=200, null=True)
    duration = models.CharField(max_length=200, null=True)
    casting_type = models.CharField(max_length=50, choices=CASTING_TYPE_CHOICES, null=True)
    ease_of_creation = models.BooleanField(default=True)
    target = models.TextField(null=True)
    school_of_magic = models.CharField(
        max_length=100, choices=SCHOOL_CHOICES, blank=True, null=True
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True)

    def __str__(self):
        return self.name


# Defines table Skill for many-to-many relationshop to Monster
class Skill(BaseAbility):
    """Model for skills including combat skills."""
    specialization = models.BooleanField(default=False)


# Defines table CombatSkill for many-to-many relationshop to Monster
class CombatSkill(BaseAbility):
    """Model for skills including combat skills."""
    specialization = models.BooleanField(default=False)


# Defines SpecialAbility for many-to-many relationshop to Monster
class SpecialAbility(BaseAbility):
    """Model for special abilities."""
    pass


# Defines Treasure for many-to-many relationshop to Monster
class Treasure(models.Model):
    """Model for treasures."""
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


# Monster model, does not include derivitive stats such as AC
class Monster(models.Model):
    """Model for monsters, excluding derivative stats like AC."""
    
    # Descriptive stats
    name = models.CharField(max_length=200)
    description = models.TextField()
    species = models.CharField(max_length=200)
    size = models.CharField(max_length=100)
    environment = models.CharField(max_length=200)
    chance_to_appear = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    tameable = models.BooleanField(default=False)
    befriendable = models.BooleanField(default=False)

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

    # Many-to-many relationships
    abilities = models.ManyToManyField(Ability)
    immunities_or_resistances = models.ManyToManyField(ImmunityOrResistanceOrWeak)
    spells = models.ManyToManyField(Spell)
    skills = models.ManyToManyField(Skill)
    special_abilities = models.ManyToManyField(SpecialAbility)
    harvested_materials = models.ManyToManyField(Material)
    treasure = models.ManyToManyField(Treasure)

    def __str__(self):
        return self.name