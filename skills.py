from array import array
from calendar import c
from cmath import atan
from itertools import count
from msilib import datasizemask
from xmlrpc.client import MAXINT
import settings
import db_data
from random import randrange
import card

#AttackAllEnemies +
#AttackInsrRound +
#CompletlyHealsOwnersCreatures +
#DealDamageToMostHitPointedOpponentsCreature +
#DealDamageToNeigboringSlots + 
#DealDamageToOpponentEveryRound +
#DealDamageToOpposingSlot +
#DealDamageToOwnerEveryRound +
#DealsDamageToAllOpponentsCreaturesEachTurn +
#ReducesRandomOwnersPowerEachTurn +
#DealsDamageToNewcomers +
#DealsDamageToOpponentAndHisCreaturesEqualOwnerElementPower +
#DealsDamageToOpponentEqualsSpecialElementManaEachTurn +
#DealsDamageToOpponentFrom1To6 +
#DealsDamageToOpponentsCreatureByTheirsCostsAtSummoning +
#DealsDamageToOppositeSlotHalflife +
#DealsDamageToRandomOpponentsCreature +
#DecreaseOpponentPowersEachTurn +
#DecreasesAllOpponentsPowersWhenKilled +
#DestroysWeakOpponentsCreaturesEachTurnEnd +
#DoDamageAtSummoningToAll +
#DoDamageAtSummoningToOpponent +
#Elemental +
#DoDamageAtSummoningToOpponentAndHisCards +
#EarnDeathPowerOnOpponentsCreatureDeath +
#GiantSpiderSkill +
#GivesRandomPowerWhenAnyCreatureDies +
#GotDamageBonusByNeighboring  +
#MovesToEmptySlotIfOppositingSlotIsNotEmpty +
#GriffinSkill +
#HealEveryone +
#HealOwnerEachTurn +
#HealPlayerAtSummoning +
#HealsNeighboringOnSummoning +
#HealsOwnerEachTurnFrom1To6 +
#HealsOwnersCreaturesAtSummoning +
#Horror +
#IgnoredDamageLessThan +
#IncreaseElementPowerBy1EachTurn +
#DoDamageAtSummoningToOpponentsCards +
#DoDamageToOpponentAtSummoning +
#IncreaseNeighborAttackBy +
#IncreaseOpponentsCardsCost +
#IncreaseOpponentsCardsCostPermanently -
#IncreaseOwnersCreaturesAttack +
#IncreaseOwnersPowers +
#IncreasePowerOnSummoningBy2 +
#IncreasePowerOnSummoningBy3 +
#IncreasesOpponentsSpellsCosts -
#IncreaseSpellsDamage -
#IncreasesPowerBy2WhenDying +
#IncreasesRandomOwnersPowerEachTurn +
#KillsCheapestOpponentsCardTypeWhenAttacksEmptySlot +
#MagicImmune -
#MaxRecievedDamageIs +
#Mindstealer +
#MovesToRandomSlotEachTurn - MovesToEmptySlotIfOppositingSlotIsNotEmpty
#StunsOppositingSlotEachTurn +
#MustBeSummonedIntoBusySlot -
#NeighborsAttacksOnSummoning
#None
#Phoenix
#ProtectsNeighboringBy
#ReduceDamageToOwnerByHalf
#ReducedOpponentsPowers
#ReflectsDamageToOpponent
#Regeneration
#SpellsDamageIncreaseBy50Percentage
#Stun
#StunsOppositSlotOnSummoning
#SummonedSoldierToRandomSlotEachTurn
#SummonsClonesToNeighboringSlots
#TakesDamageToOwnerToItselfInstead
#TakesToOwnerPowersOfAllKindAtSummoning
#Vampire


#TODO
#Check if card is dead
#Check if head is dead
#All in main file
#Add increase each element apart from each other and delete of increase when elemnt dies

def player_cards_attack(atacking_player_played_cards, player_two_played_cards, turn, atacking_player_head, player_two_head):
    if turn == settings.Players.atacking_player:
        attacking_player = atacking_player_played_cards
        attacked_player = player_two_played_cards
        attacking_player_head = atacking_player_head
        attacked_player_head = player_two_head 
    else:
        attacking_player = player_two_played_cards
        attacked_player = atacking_player_played_cards
        attacking_player_head = player_two_head
        attacked_player_head = atacking_player_head 
    #processData
    #CallFunctions


def __attack_all_enemies(attacking_player_card, attacked_player, attacked_player_head):
        for card in attacked_player:
            if card:
                if not attacking_player_card.stun:
                    card.healt -= attacking_player_card.damage
                if attacking_player_card.stun:
                    attacking_player_card.stun = False
            else:
                attacked_player_head.hp -= attacking_player_card.damage


def __attack_in_1st_round(attacking_player_card, attacked_player, attacked_player_head):
    for card in attacked_player:
            if card:
                card.healt -= attacking_player_card.damage
                if attacking_player_card.stun:
                    attacking_player_card.stun = False
            else:
                attacked_player_head.hp -= attacking_player_card.damage


def __completly_heals_owners_creatures(attacking_player):
    for card in attacking_player:
        card.health = db_data.get_healt(card.inner_name)


def __deal_damage_to_most_hit_pointed_opponents_creature(attacking_player_card, attacked_player):
    healhiest_creature = None
    for card in attacked_player:
        if card:
            if not healhiest_creature:
                healhiest_creature = card
            else:
                if card.health > healhiest_creature.healt:
                    healhiest_creature = card

    if not healhiest_creature:
        healhiest_creature.healt -= attacking_player_card.damage


def __deal_damage_to_neigboring_slots(attacking_player_card, attacking_player, damage):
    for i in range(len(attacking_player)):
        if attacking_player_card == attacking_player[i]:
            index = i

    if i > 0:
        attacking_player[i - 1].health -= damage
    if i < len(attacking_player) - 1:
        attacking_player[i + 1].health -= damage


def __deal_damage_to_opponent_every_round(attacked_player_head, damage):
    attacked_player_head.hp -= damage


def __deal_damage_to_opposing_slot(attacked_player_card, damage):
    attacked_player_card.health -= damage


def __deal_damage_to_owner_every_round(attacking_player_head, damage):
    attacking_player_head.hp -= damage


def __deals_damage_to_all_opponents_creatures_each_turn(attacked_player, damage):
    for card in attacked_player:
        if card:
            card.health -= damage


def __reduces_random_owners_power_each_turn(attacking_player_mana, reduce_amount):
    index = randrange(len(attacking_player_mana))
    counter = 0
    for key in attacking_player_mana.items():
        if counter == index:
            attacking_player_mana[key] -= reduce_amount
            break
        counter += 1


def __deals_damage_to_newcomers(attacked_player, damage):
    for card in attacked_player:
        if card.stun:
            card.health -= damage


def __deals_damage_to_opponent_and_his_creatures_equal_owner_element_power(attacking_player_mana, element_title,
 attacked_player, attacked_player_head):
    damage_amount = attacking_player_mana[element_title]
    if damage_amount > 10:
        damage_amount = 10
    
    for card in attacked_player:
        if card:
            card.health -= damage_amount
    
    attacked_player_head.hp -= damage_amount


def __deals_damage_to_opponent_equals_special_element_mana_each_turn(attacking_player_mana, element_title, attacked_player_head):
    damage_amount = attacking_player_mana[element_title]

    attacked_player_head.hp -= damage_amount


def __deals_damage_to_opponent_from_1To6(attacked_player_head):
    damage_amount = randrange(1, 7)

    attacked_player_head.hp -= damage_amount


def __deals_damage_to_opponents_creature_by_theirs_costs_at_summoning(attacked_player, cost):
    for card in attacked_player:
        if card:
            card.health -= cost


def __deals_damage_to_opposite_slot_halflife(creature_index, attacked_player):
    attacked_player[creature_index].health -= attacked_player[creature_index].health // 2


def __deals_damage_to_random_opponents_creature(attacked_player, damage):
    creatures_count = 0

    for card in attacked_player:
        if card:
            creatures_count += 1

    random_index = randrange(creatures_count)
    counter = 0
    for i in range(creatures_count):
        if attacked_player[i]:
            if counter == random_index:
                attacked_player[i].health -= damage
            else:
                counter += 1


def __decrease_opponent_powers_each_turn(attacked_player_mana, decrease_amount):
    for key in attacked_player_mana.items():
        attacked_player_mana[key] -= decrease_amount


def __decreases_all_opponents_powers_when_killed(attacking_player_mana, decrease_amount):
    for key in attacking_player_mana.items():
        attacking_player_mana[key] -= decrease_amount


def __destroys_weak_opponents_creatures_each_turn_end(attacked_player, less_than):
    for card in attacked_player:
        if card:
            if card.health <= less_than:
                card.health = 0


def __do_damage_at_summoning_to_all(attacked_player, damage_amount):
    for card in attacked_player:
        if card:
            card.health -= damage_amount


def __do_damage_at_summoning_to_opponent(attacked_player_head, damage_amount):
    attacked_player_head.hp -= damage_amount


def __elemental(element_title, mana_increase_player):
    for key in mana_increase_player.items():
        if key == element_title:
            mana_increase_player[key] += 1


def __do_damage_at_summoning_to_opponent_and_his_cards(attacked_player, attacked_player_head, damage_amount):
    for card in attacked_player:
        if card:
            card.health -= damage_amount

    attacked_player_head.hp -= damage_amount


def __earn_death_power_on_opponents_creature_death(attacking_player_mana):
    attacking_player_mana["Death"] += 1


def __giant_spider_skill(attacking_player, creature_index, attacking_player_space, screen):
    if not attacking_player[creature_index - 1]:
        right_spider = card.Card(screen, "Forest spider", 0, 0)
        attacking_player_space.is_empty[creature_index - 1] = False
        new_card = card.ActiveCard(screen, right_spider)
        new_card.rect.x = attacking_player_space.squares[creature_index - 1].x
        new_card.rect.y = attacking_player_space.squares[creature_index - 1].y
        attacking_player[creature_index - 1] = new_card
    if not attacking_player[creature_index + 1]:
        right_spider = card.Card(screen, "Forest spider", 0, 0)
        attacking_player_space.is_empty[creature_index + 1] = False
        new_card = card.ActiveCard(screen, right_spider)
        new_card.rect.x = attacking_player_space.squares[creature_index + 1].x
        new_card.rect.y = attacking_player_space.squares[creature_index + 1].y
        attacking_player[creature_index + 1] = new_card


def __gives_random_power_when_any_creature_dies(attacking_player_mana, increase_amount):
    index = randrange(len(attacking_player_mana))
    counter = 0

    for key in attacking_player_mana.items():
        if counter == index:
            attacking_player_mana[key] += increase_amount
            break
        else:
            counter += 1

        
def __got_damage_bonus_by_neighboring(creature_index, amount_damage_bonus, attacking_player):
    attacking_player[creature_index].health = db_data.get_damage(attacking_player[creature_index].inner_name)

    if attacking_player[creature_index - 1]:
        attacking_player[creature_index].damage += amount_damage_bonus

    if attacking_player[creature_index + 1]:
        attacking_player[creature_index].damage += amount_damage_bonus


def __moves_to_empty_slot_if_oppositing_slot_is_not_empty(creature_index, attacking_player, attacked_player, attacking_player_space):
    if attacked_player[creature_index]:
        for i in range(len(attacking_player)):
            if not attacking_player[i]:
                attacking_player_space.is_empty[creature_index] = True
                attacking_player[i] = attacking_player[creature_index]
                attacking_player[creature_index] = None

                attacking_player_space.is_empty[i] = False
                attacking_player[i].rect.x = attacking_player_space.squares[i].x
                attacking_player[i].rect.y = attacking_player_space.squares[i].y


def __griffin_skill(attacking_player_mana, attacked_player_head):
    if attacking_player_mana["Air"] >= 5:
        attacked_player_head.hp -= 5


def __heal_everyone(attacking_player, attacking_player_head, heal_amount):
    for card in attacking_player:
        if card:
            card.health += heal_amount

    attacking_player_head.hp += heal_amount


def __heal_owner_each_turn(attacking_player_head, heal_amount):
    attacking_player_head.hp += heal_amount


def __heal_player_at_summoning(attacking_player_head, heal_amount):
    attacking_player_head.hp += heal_amount


def __heals_neighboring_on_summoning(attacking_player, heal_amount, creature_index):
    if attacking_player[creature_index - 1]:
        attacking_player[creature_index - 1].health += heal_amount

    if attacking_player[creature_index + 1]:
        attacking_player[creature_index + 1].health += heal_amount


def __heals_owner_each_turn_from_1To6(attacking_player_head):
    amount = randrange(1, 7)

    attacking_player_head.hp += amount


def __heals_owners_creatures_at_summoning(attacking_player, heal_amount):
    for card in attacking_player:
        if card:
            card.health += heal_amount


def __horror(attacked_player, cost):
    for card in attacked_player:
        if card and card.cost < cost:
            card.stun = True


def __ignored_damage_less_than(attacking_player, creature_index, dealed_damagae, less_than):
    if dealed_damagae <= less_than:
        attacking_player[creature_index].health += dealed_damagae

    else:
        attacking_player[creature_index].health += less_than


def __IncreaseElementPowerBy1EachTurn(element_title, mana_increase_player_test):
    mana_increase_player_test[element_title] += 1


def __do_damage_at_summoning_to_opponents_cards(attacked_player, damage_amount):
    for card in attacked_player:
        card.health -= damage_amount


def __do_damage_to_opponent_at_summoning(attacked_player_head, damage_amount):
    attacked_player_head.hp -= damage_amount


def __increase_neighbor_attack_by(attacking_player, creature_index, increase_amount):
    if attacking_player[creature_index - 1]:
        attacking_player.damage += increase_amount

    if attacking_player[creature_index + 1]:
        attacking_player.damage += increase_amount


def __increase_opponents_cards_cost(attacked_player_deck, increase_amount):
    for card in attacked_player_deck:
        if card:
            card.cost += increase_amount


def __increase_owners_creatures_attack(attacking_player, increase_amount):
    for card in attacking_player:
        if card:
            card.damage += increase_amount


def __increase_owners_powers(attacking_player_mana, increase_amount):
    for key in attacking_player_mana.items():
        attacking_player_mana[key] += increase_amount


def __increase_power_on_summoning_by2(attacking_player_mana, element_title):
    attacking_player_mana[element_title] += 2


def __increase_power_on_summoning_By3(attacking_player_mana, element_title):
    attacking_player_mana[element_title] += 3


def __increases_opponents_spells_costs():
    i = 0


def __increase_spells_damage():
    i = 0


def __increases_power_by2_when_dying(element_title, attacking_player_mana):
    attacking_player_mana[element_title] += 2


def __increases_random_owners_power_each_turn(attacking_player_mana, increase_amount):
    random_element = randrange(len(attacking_player_mana))

    attacking_player_mana[random_element] += increase_amount


def __kills_cheapest_opponents_card_type_when_attacks_empty_slot(attacked_player, attacked_player_space):
    cheapest = MAXINT
    index_cheapest_card = MAXINT

    for i in range(len(attacked_player)):
        if attacked_player[i] and attacked_player[i].cost < cheapest:
            cheapest = attacked_player[i].cost
            index_cheapest_card = i

    attacked_player_space.is_empty[index_cheapest_card] = True
    attacked_player[index_cheapest_card] = None


def __magic_immune():
    i = 0
    

def __max_recieved_damage_is(creature_index, attacked_player, damage_amount):
    attacked_player[creature_index].health -= damage_amount


def __mindstealer(attacking_player, attacked_player):
    for i in range(len(attacked_player)):
        if attacked_player[i].inner_name == "Mindstealer":
            attacking_player[i].healt -= attacked_player[i].damage


def __stuns_oppositing_slot_each_turn(creature_index, attacked_player):
    attacked_player[creature_index].stun = True


"""def __must_be_summoned_into_busy_slot():
    """