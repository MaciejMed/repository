import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='/')


TOKEN = ''

builds = {
        'Quinn': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-quinnads-challenger-season-13-quinn-guide-new-items-568972',
            'mid': 'https://www.mobafire.com/league-of-legends/build/patch-13-12-sheppardlols-quinn-mid-guide-570563',
        },
        'Cassiopeia': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/new-season-13-13-17-updated-cassiopeia-the-poison-queen-of-midlane-562793',
        },
        'Zac': {
            'top': 'https://www.mobafire.com/league-of-legends/build/season-13-zac-top-610888',
            'jungle': 'https://www.mobafire.com/league-of-legends/build/rank-4-zac-euw-erknaites-season-13-zac-guide-patch-13-17-620887',
        },
         'Vayne': {
            'bot': 'https://www.mobafire.com/league-of-legends/build/season-13-vayne-guide-13-17-patch-updated-ready-487606',
        },
         'Kayle': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-3-ad-kayle-top-mid-let-all-enemys-explode-at-once-602147',
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-3-ad-kayle-top-mid-let-all-enemys-explode-at-once-602147',
        },
         'Garen': {
            'top': 'https://www.mobafire.com/league-of-legends/build/paul-chungs-master-garen-guide-583854',
        },
         'Tryndamere': {
            'top': 'https://www.mobafire.com/league-of-legends/build/best-tryndamere-world-challenger-guide-by-rangerzx-593112',
            'mid': 'https://www.mobafire.com/league-of-legends/build/in-depth-rank-1-challenger-tryndamere-by-yasukeh-539890',
        },
         'Malphite': {
            'top': 'https://www.mobafire.com/league-of-legends/build/s13-wormmaws-guide-for-malphite-519862',
            'mid': 'https://www.mobafire.com/league-of-legends/build/season-13-ap-one-shot-malphite-mid-builds-and-runes-620312',
        },
         'Dr. Mundo': {
            'top': 'https://www.mobafire.com/league-of-legends/build/phrxshns-guide-to-rework-dr-mundo-13-18-where-ever-he-goes-581823',
            'jungle': 'https://www.mobafire.com/league-of-legends/build/s13-wildebobs-insane-smurf-1v9-dr-mundo-jungle-guide-589384',
        },
         'Poppy': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-11-the-only-hero-master-poppy-top-guide-606114',
            'jungle': 'https://www.mobafire.com/league-of-legends/build/13-11-no-dashing-around-diamond-poppy-jungle-guide-587673',
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-poppy-support-tank-items-suck-so-ill-just-build-enchanter-items-609307',
        },
         'Kled': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-the-ultimate-s13-challenger-kled-guide-564240',
            'mid': 'https://www.mobafire.com/league-of-legends/build/mid-kled-the-league-of-legends-don-quixote-596544',
        },
         'Illaoi': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-illaoi-otp-advanced-guide-618052',
        },
         'Olaf': {
            'top': 'https://www.mobafire.com/league-of-legends/build/life-steal-olaf-top-patch-13-17-501585',
            'jungle': 'https://www.mobafire.com/league-of-legends/build/olafend-urge-to-kill-rising-13-16-577240',
        },
         'Camille': {
            'top': 'https://www.mobafire.com/league-of-legends/build/raens-camille-tips-amp-build-569910',
        },
         'Aatrox': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-become-the-world-ender-grand-masters-aatrox-guide-601245',
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-17-aatrox-mega-guide-5-8m-diamond-1-worldwide-mp-otp-589188',
        },
         'Singed': {
            'top': 'https://www.mobafire.com/league-of-legends/build/phrxshns-in-depth-guide-to-singed-13-18-evenshroud-nerf-sadge-578305',
            'mid': 'https://www.mobafire.com/league-of-legends/build/gm-deag7s-season-13-singed-guide-606706',
        },
         'Urgot': {
            'top': 'https://www.mobafire.com/league-of-legends/build/goliathgames-ultimate-guide-to-urgot-tips-on-every-matchup-3m-mastery-554383',
        },
         'Fiora': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-16-all-matchups-top-15-euw-potents-4m-mastery-challenger-fiora-guide-rank-1-fiora-euw-coaching-available-607140',
        },
         'Maokai': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-euw-lathyrus-challenger-guide-on-how-to-meowkai-support-567295',
        },
         'Nasus': {
            'top': 'https://www.mobafire.com/league-of-legends/build/assassin-nasus-613714',
            'mid' : 'https://www.mobafire.com/league-of-legends/build/13-4-desperate-nasus-challenger-nasus-mid-in-depth-guide-605021',
            'support' : 'https://www.mobafire.com/league-of-legends/build/nemmegyle-a-jade-support-nasus-guide-scooby-spamming-wither-557165',
        },
         'Warwick': {
            'top': 'https://www.mobafire.com/league-of-legends/build/phrxshns-guide-to-warwick-13-18-chill-wolfman-581230',
            'jungle': 'https://www.mobafire.com/league-of-legends/build/13-17-former-s12-rank-3-ww-na-163-lp-masters-peak-jungle-guide-620420',
        },
         'Sylas': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/quot-no-prison-can-hold-me-quot-the-perfect-sylas-guide-626226',
        },
         'Rammus': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/my-immortal-rammus-build-492829',
        },
         'ChoGath': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-addition-to-baloris-chogod-threats-amp-tips-564663',
            'mid': 'https://www.mobafire.com/league-of-legends/build/season-13-sakuritou-challenger-rank-1-cho-world-guide-609864',
        },
         'Ornn': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-loadingscreen-top-guide-575652',
        },
         'Malzahar': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-16-rank-1-malzahar-complete-guide-by-coach-xblademojo-608062',
        },
         'Renekton': {
            'top': 'https://www.mobafire.com/league-of-legends/build/season-13-masters-top-renekton-guide-china-ionia-server-601981',
            'mid': 'https://www.mobafire.com/league-of-legends/build/musiccrocs-midlane-croc-627464',
        },
         'Udyr': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-ragos-udyr-toplane-in-depth-guide-621114',
            'jungle': 'https://www.mobafire.com/league-of-legends/build/13-17-ragos-udyr-jungle-in-depth-guide-619574',
        },
         'Sett': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-autolykuss-challenger-sett-guide-594869',
            'mid': 'https://www.mobafire.com/league-of-legends/build/my-immortal-sett-build-all-lanes-top-mid-jungle-bot-583887',
            'bot': 'https://www.mobafire.com/league-of-legends/build/my-immortal-sett-build-all-lanes-top-mid-jungle-bot-583887',
        },
         'Darius': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-just1kbs-darius-guide-540023',
        },
         'Trundle': {
            'top': 'https://www.mobafire.com/league-of-legends/build/trundle-top-guide-by-trundletop1-596663',
            'jungle': 'https://www.mobafire.com/league-of-legends/build/coccaas-trundle-jungle-guide-updated-for-season-13-627173',
        },
         'Pantheon': {
            'top': 'https://www.mobafire.com/league-of-legends/build/stand-up-face-me-again-pantheon-top-explained-616285',
            'mid': 'https://www.mobafire.com/league-of-legends/build/midtheon-pantheon-mid-guide-in-depth-matchups-624921',
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-support-pantheon-tier-list-616923',
        },
         'Ryze': {
            'top': 'https://www.mobafire.com/league-of-legends/build/raens-ryze-tips-amp-build-567878',
            'mid': 'https://www.mobafire.com/league-of-legends/build/s13-masters-ryze-guide-runes-builds-amp-all-613839',
        },
         'Shyvana': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/the-best-shyvana-guide-for-s13-ap-ad-and-tank-pick-your-poison-they-all-work-572053',
        },
         'Mordekaiser': {
            'top': 'https://www.mobafire.com/league-of-legends/build/raens-mordekaiser-tips-amp-build-569896',
        },
         'Shen': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-xpetus-challenger-shen-guide-582399',
            'support': 'https://www.mobafire.com/league-of-legends/build/freyas-shinobi-support-guide-589877',
        },
         'Tahm Kench': {
            'top': 'https://www.mobafire.com/league-of-legends/build/masters-otp-1-kench-eune-guide-read-notes-for-explanation-in-depth-tips-for-all-matchups-626518',
            'support': 'https://www.mobafire.com/league-of-legends/build/13-4-the-kench-compendium-598679',
        }, 
         'Irelia': {
            'top': 'https://www.mobafire.com/league-of-legends/build/season-13-masters-top-irelia-guide-china-ionia-server-601727',
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-17-eriosuns-master-tier-complete-irelia-guide-season-13-updated-598099',
        },
         'Rengar': {
            'top': 'https://www.mobafire.com/league-of-legends/build/best-rengar-na-13-16-more-lethality-buffs-600044',
            'jungle': 'https://www.mobafire.com/league-of-legends/build/new-items-out-13-17-multiseason-challenger-pusipuu-guide-in-depth-s13-589480',
        },
         'Wukong': {
            'top': 'https://www.mobafire.com/league-of-legends/build/my-full-lethality-armor-penetration-amp-pta-wukong-build-489742',
            'jungle': 'https://www.mobafire.com/league-of-legends/build/13-17-perfectpowers-jungle-wukong-guide-622036',
        },
         'Naafiri': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-naafiri-top-jungle-bruiser-build-threats-added-on-a-regular-basis-627363',
            'jungle': 'https://www.mobafire.com/league-of-legends/build/13-17-best-jg-naafiri-guide-627321',
            'mid': 'https://www.mobafire.com/league-of-legends/build/how-to-be-ahead-of-the-pack-with-naafiri-mid-jng-all-matchups-624734',
        },
         'Lillia': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/s13-lillia-mid-gigachad-mid-621305',
            'jungle': 'https://www.mobafire.com/league-of-legends/build/13-17-s11-challenger-how-to-take-over-as-lillia-578273',
        },
         'Swain': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-swain-mid-ultimate-guide-top-bot-amp-support-also-covered-613182',
            'mid': 'https://www.mobafire.com/league-of-legends/build/new-season-13-13-16-updated-swain-is-the-god-of-midlane-pain-601216',
            'support': 'https://www.mobafire.com/league-of-legends/build/13-5-swain-support-build-guide-601349',
        },
         'Heimerdinger': {
            'top': 'https://www.mobafire.com/league-of-legends/build/buzz-buzz-612588',
            'mid': 'https://www.mobafire.com/league-of-legends/build/new-season-13-17-midlane-master-tier-8-million-mastery-heimerdinger-519454',
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-support-heimerdinger-tier-list-620111',
        },
         'Volibear': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-challenger-volibear-top-guide-609641',
            'jungle': 'https://www.mobafire.com/league-of-legends/build/guide-to-off-meta-volibear-jungle-builds-627787',
        },
         'Riven': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-become-a-riven-god-404727',
        },
         'Rumble': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/patch-13-13-through-the-fire-and-the-flames-by-nahde-568169',
        },
         'Gangplank': {
            'top': 'https://www.mobafire.com/league-of-legends/build/oh-captain-my-captain-520854',
            'mid': 'https://www.mobafire.com/league-of-legends/build/12-23-the-gangplank-compendium-all-roles-564821',
        },
         'Akali': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-challenger-mid-top-akali-guide-by-daito-amp-luner-in-depth-627712',
            'mid': 'https://www.mobafire.com/league-of-legends/build/anguishs-masters-akali-mid-top-s13-guide-patch-13-17-every-matchup-item-rune-explained-625064',
        },
         'Gnar': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-2-diamond-gnar-guide-thing-in-the-ice-season-13-updating-546377',
        },
         'Jayce': {
            'top': 'https://www.mobafire.com/league-of-legends/build/s13-the-hammer-bible-the-second-coming-of-hextech-jesus-606026',
        },
         'Teemo': {
            'top': 'https://www.mobafire.com/league-of-legends/build/the-passionate-guide-to-teemo-456667',
            'support': 'https://www.mobafire.com/league-of-legends/build/the-only-teemo-support-guide-you-will-need-625403',
        },
         'Yone': {
            'top': 'https://www.mobafire.com/league-of-legends/build/rank-1-global-yone-guide-saitamaro-the-yone-bible-s13-will-get-updated-regularly-627809',
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-13-tempests-challenger-yone-guide-in-depth-590183',
        },
         'Sion': {
            'top': 'https://www.mobafire.com/league-of-legends/build/strategically-minded-sion-tank-ad-thebausffs-builds-584534',
        },
         'Gwen': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-menace-to-lol-gwen-revamped-598867',
            'mid': 'https://www.mobafire.com/league-of-legends/build/gwen-midlane-13-16-best-high-elo-gwen-build-611339',
        },
         'Yorick': {
            'top': 'https://www.mobafire.com/league-of-legends/build/my-fleet-conqueror-yorick-monstrous-build-528679',
        },
         'Jax': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-thisispatriks-in-depth-jax-guide-503356',
            'jungle': 'https://www.mobafire.com/league-of-legends/build/jax-build-598177',
        },
         'Vladimir': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/elite500-70-wr-top-200-korea-midlane-vladimir-guide-patch-13-17-591779',
        },
         'Yasuo': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-unforgivens-in-depth-yasuo-mid-top-guide-529530',
            'mid': 'https://www.mobafire.com/league-of-legends/build/7m-mastery-points-yasuo-best-build-for-patch-13-17-529033',
        },
         'Kalista': {
            'bot': 'https://www.mobafire.com/league-of-legends/build/13-17-7eyesnoskills-kalista-guide-612723',
        },
         'Kennen': {
            'top': 'https://www.mobafire.com/league-of-legends/build/season-13-ap-ad-kennen-all-roles-575084',
            'mid': 'https://www.mobafire.com/league-of-legends/build/kennen-guide-xoany-627286',
        },
         'Sejuani': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-13-the-5-position-flex-pick-seriously-544668',
            'jungle': 'https://www.mobafire.com/league-of-legends/build/13-17-challenger-na-amp-euw-in-depth-sejuani-guide-tank-and-utility-597926',
        },
         'Gragas': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-bomba-gragas-guide-by-sloppy-walrus-580545',
            'jungle': 'https://www.mobafire.com/league-of-legends/build/preseason-13-extensive-guide-to-gragas-540914',
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-17-pretends-nuclear-ap-gragas-mid-guide-607120',
            'support': 'https://www.mobafire.com/league-of-legends/build/13-16-gragas-supp-guide-616889',
        },
         'Xin Zahao': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/xin-zhaofend-to-the-arena-13-17-553218',
        },
         'Skarner': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/13-17-the-skarner-bible-by-lans-rank-1-skarner-615052',
        },
         'K Sante': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-ksante-mains-guide-624722',
        },
         'Jarvan': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/s13-destroy-soloq-with-jarvan-iv-udysof-challenger-j4-564584',
        },
         'Rek Sai': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/s13-lordgrox-high-elo-reksai-guide-595303',
        },
         'Nocturne': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/12-23-nocturne-guide-615003',
        },
         'Ivern': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/season-13-challenger-ivern-guide-4-million-mastery-621914',
            'support': 'https://www.mobafire.com/league-of-legends/build/challenger-ivern-support-guide-587026',
        },
         'Fiddlestick': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/unlock-your-jungle-potential-with-fiddlesticks-a-guide-from-the-former-1-fiddlesticks-player-in-the-world-589051',
            'support': 'https://www.mobafire.com/league-of-legends/build/how-i-became-1-fiddle-world-support-571193',
        },
         'Evelynn': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/splashs-1-6klp-challenger-euw-evelynn-guide-updated-for-s13-work-in-progress-618084',
        },
         'Amumu': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/ap-amumu-junglee-585995',
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-amumu-support-tier-list-615048',
        },
         'Kha Zix': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/sybr-rank-1-challenger-khazix-guide-season-13-571980',
        },
         'Ekko': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/ekko-jungle-guide-in-depth-updated-583494',
            'mid': 'https://www.mobafire.com/league-of-legends/build/power-leons-guide-for-ekko-players-in-mid-lane-556239',
        },
         'Taliyah': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/patch-13-15-taliyah-from-gold-player-garena-server-mid-jungler-613089',
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-17-taliyah-mid-ultimate-guide-in-depth-bot-support-amp-jungle-also-covered-612959',
            'support': 'https://www.mobafire.com/league-of-legends/build/taliyah-support-by-a-taliyah-support-main-621554',
        },
         'Karthus': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/season-13-challenger-karthus-jgl-guide-560458',
            'mid': 'https://www.mobafire.com/league-of-legends/build/2-4-million-mastery-lane-karthus-guide-season-13-579191',
        },
         'Rell': {
            'top': 'https://www.mobafire.com/league-of-legends/build/13-17-unbreakable-rell-top-guide-619986',
            'support': 'https://www.mobafire.com/league-of-legends/build/challenger-rell-support-guide-586775',
        },
         'Kayn': {
            'Jungle': 'https://www.mobafire.com/league-of-legends/build/racticks-1m-mastery-13-17-updated-detailed-kayn-guide-for-all-situation-589676',
        },
        'Bel Veth': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/racticks-13-17-updated-detailed-belveth-guide-614086',
        },
        'Diana': {
            'Jungle': 'https://www.mobafire.com/league-of-legends/build/s13-jungle-disastrous-diana-going-offensive-or-defensive-303837',
        },
        'Graves': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/13-17-arfreezys-guide-to-graves-jungle-585199',
        },
        'Shaco': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/13-17-facets-ultimate-in-depth-ad-shaco-jungle-guide-biiig-patch-items-runes-updated-606325',
            'support': 'https://www.mobafire.com/league-of-legends/build/13-16-shaco-support-guide-2mil-sup-one-trick-598078',
        },
        'Vi': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/how-to-smash-rocks-551110',
        },
        'Talon': {
             'mid' : 'https://www.mobafire.com/league-of-legends/build/season-13-coldsongs-talon-guide-556488',
            'jungle': 'https://www.mobafire.com/league-of-legends/build/split-2-13-16-kaostanzas-talon-jungle-guide-challenger-613498',
        },
        'Nidalee': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/13-16-rank-1-nidalee-euw-majds-challenger-nidalee-guide-in-depth-622877',

        },
        'Elise': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/season-13-split-2-rank-1-elise-ultimate-comprehensive-guide-to-elise-589620',
        },
        'Master Yi': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/s13-the-best-master-yi-guide-520380',
        },
        'Viego': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/season-13-patch-13-12-elekktros-masters-jungle-viego-guide-tri-force-meta-605091',
        },
        'Nunu Willump': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/13-11-snowballs-challenger-tank-ap-nunu-guide-hi-589817',
        },
        'Kindred': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/13-16-play-maker-build-by-yed-530976',
        },
        'Hecarim': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/building-is-outdated-expert-hecarim-guide-by-riealone-571918',
        },
        'Lee Sin': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/13-17-former-rank-1-lee-sin-na-truck-drivers-lee-sin-guide-in-depth-610673',
        },
        'Zed': {
            'jungle': 'https://www.mobafire.com/league-of-legends/build/13-5-challenger-zed-jungle-guide-free-lp-616618',
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-14-max-depth-master-zed-guide-598849',
        },
        'Qiyana': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/how-to-carry-with-qiyana-updated-590371',
        },
        'Aurelion Sol': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-7-vicksys-reworked-master-asol-guide-529167',
        },
        'Anivia': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/new-season-13-13-16-updated-masters-guide-to-midlane-anivia-s-tier-pick-559691',
            'support': 'https://www.mobafire.com/league-of-legends/build/challenger-anivia-support-guide-581275',
        }, 
        'Zilean': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/gla-ten-zilean-mid-guide-562632',
        },   
        'Vex': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/ziannis-challenger-vex-guide-603903',
            'support': 'https://www.mobafire.com/league-of-legends/build/challenger-vex-support-guide-602408',
        },   
        'Xerath': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-17-climb-responsibly-with-xerath-social-distance-mage-570556',
            'support': 'https://www.mobafire.com/league-of-legends/build/the-only-xerath-support-guide-you-will-need-624581',
        },   
        'Orianna': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/season-13-13-16-updated-master-tier-midlane-orianna-the-balls-hurt-561083',
        },   
        'Kassadin': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-16-rank-1-kassadin-complete-guide-by-coach-xblademojo-602685',
        },   
        'Viktor': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/patch-13-17-my-viktors-build-all-and-rare-matchups-604795',
        },  
        'Neeko': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/curious-chameleon-on-mid-s12-guide-13-8-work-in-progress-for-13-9-587131',
            'support': 'https://www.mobafire.com/league-of-legends/build/challenger-neeko-support-guide-561241',
            'top' : 'https://www.mobafire.com/league-of-legends/build/13-16-masters-ad-neeko-top-guide-573397'
        },    
        'Lux': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-17-mid-apc-light-em-up-im-on-fiyaa-luxe-n-style-460573',
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-support-light-em-up-im-on-fiyaa-luxe-n-style-530121',
        },  
        'Lissandra': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/new-season-13-updated-13-15-the-midlane-ice-queen-of-death-603019',
            'support': 'https://www.mobafire.com/league-of-legends/build/lissandra-support-a-generous-queen-that-helps-warding-guide-596927',
        },  
        'Seraphine': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-17-cupics-challenger-1000-lp-seraphine-guide-s12-586687',
            'bot': 'https://www.mobafire.com/league-of-legends/build/apc-queen-slayaphine-614370',
            'support': 'https://www.mobafire.com/league-of-legends/build/seraphine-support-guide-583193',
        },  
        'Brand': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/patch-13-17-how-to-play-brand-mid-builds-matchups-50-done-609921',
            'support': 'https://www.mobafire.com/league-of-legends/build/13-16-bizzleberrys-season-13-brand-support-hot-again-502033',
        },  
        'Kog Maw': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/s13-wormmaws-guide-for-ap-kogmaw-512820',
        },  
        'Ziggs': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/s13-wormmaws-guide-for-ziggs-532170',
            'bot': 'https://www.mobafire.com/league-of-legends/build/best-mage-bot-lane-ziggs-high-elo-comprehensive-guide-589994',
        },  
        'Fizz': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-17-prestigegalaxys-simple-guide-to-fizz-609483',
        },  
        'Vel Koz': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/patch-13-17-season-13-azzapps-guide-to-velkoz-mid-sup-528463',
            'support': 'https://www.mobafire.com/league-of-legends/build/patch-13-17-support-velkoz-prepared-for-everything-615002',
        },  
        'Syndra': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/patch-13-17-the-ultimate-syndra-guide-always-win-lane-100-554390',
        },  
        'Talon': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/season-13-coldsongs-talon-guide-556488',
        },  
        'Veigar': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/patch-13-17-my-veigars-build-all-matchups-607093',
            'bot': 'https://www.mobafire.com/league-of-legends/build/ziannis-veigar-guide-585002',
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-support-veigar-tier-list-616335',
        },  
        'Tristana': {
            'bot': 'https://www.mobafire.com/league-of-legends/build/13-7-how-do-you-trist-rank-1-trist-world-guide-comprehensive-614275',
        },  
        'Ahri': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-11-vicksys-master-updated-ahri-guide-553313',
        },  
        'Annie': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-6-the-dark-child-all-viable-roles-and-runes-521111',
        },  
        'Galio': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/patch-13-17-my-galios-build-mid-support-matchups-611334',
            'support': 'https://www.mobafire.com/league-of-legends/build/patch-13-17-my-galios-build-mid-support-matchups-611334',
        },  
        'Twisted Fate': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-17-s13-twisted-fate-guide-grandmaster-halfhand-584499',
        },  
        'Zoe': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/the-intensive-self-help-guide-for-everything-you-need-to-know-about-zoe-621324',
            'support': 'https://www.mobafire.com/league-of-legends/build/challenger-zoe-support-guide-571732',
        },  
        'Katarina': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-17-nyros-challenger-euw-build-amp-guide-always-updated-612060',
        },  
        'Azir': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/13-16-ascended-emperor-608618',
        },  
        'LeBlanc': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/patch-13-17-fuzzmonkeys-leblanc-guide-always-win-lane-100-523241',
            'support': 'https://www.mobafire.com/league-of-legends/build/challenger-leblanc-support-guide-598206',
        },  
        'Corki': {
            'mid': 'https://www.mobafire.com/league-of-legends/build/raens-corki-tips-amp-build-567918',
        },  
        'Varus': {
            'bot': 'https://www.mobafire.com/league-of-legends/build/the-mathematically-correct-ap-varus-mid-bot-625013',
        },  
        'Miss Fortune': {
            'bot': 'https://www.mobafire.com/league-of-legends/build/13-17-miss-fortune-critical-strike-amp-lethality-610632',
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-support-miss-fortune-tier-list-615673',
        },  
        'Ashe': {
            'bot': 'https://www.mobafire.com/league-of-legends/build/how-to-actually-play-ashe-adc-supp-613171',
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-ashe-support-tier-list-613233',
        },  
        'Twitch': {
            'bot': 'https://www.mobafire.com/league-of-legends/build/ad-amp-ap-twitch-guide-13-16-628280',
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-euw-challenger-ap-twitch-support-588469',
        },  
        'Caitlyn': {
            'bot': 'https://www.mobafire.com/league-of-legends/build/13-16-my-straightforward-guide-to-crit-caitlyn-622607',
        },  
        'Lulu': {
            'support': 'https://www.mobafire.com/league-of-legends/build/how-to-be-annoying-1-8-mil-points-all-roles-581944',
        },  
        'Yuumi': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-yuumi-support-tier-list-623601',
        },  
        'Pyke': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-ultimate-ferrari-support-574844',
        },  
        'Milio': {
            'support': 'https://www.mobafire.com/league-of-legends/build/lathyrus-official-challenger-milio-support-guide-13-17-623987',
        },  
        'Karma': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-karma-support-tier-list-611468',
        },  
        'Morgana': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-9-bizzleberrys-season-13-morgana-guide-new-build-529560',
        },  
        'Renata Glasc': {
            'support': 'https://www.mobafire.com/league-of-legends/build/lathyrus-13-17-challenger-renata-support-609588',
        },  
        'Bard': {
            'support': 'https://www.mobafire.com/league-of-legends/build/lathyrus-13-17-euw-challenger-mid-season-update-544216',
        }, 
        'Alistar': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-you-cant-milk-those-a-comprehensive-alistar-guide-623299',
        }, 
        'Braum': {
            'support': 'https://www.mobafire.com/league-of-legends/build/braum-13-17-support-guide-the-shepherd-of-adcs-486977',
        }, 
        'Thresh': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-master-thresh-support-guide-601680',
        }, 
        'Nautilus': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-hanjaros-nautilus-guide-552530',
        }, 
        'Senna': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-themistcollectors-ultimate-senna-guide-supp-adc-amp-fasting-589673',
        }, 
        'Nami': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-eunamikus-rank-1-nami-in-depth-guide-592563',
        },
        'Leona': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-leona-tank-support-610655',
        },
        'Zyra': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-16-bizzleberrys-season-13-zyra-support-guide-rerooted-536194',
        },
        'Sona': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-14-sona-guide-for-carry-support-617052',
        },
        'Rakan': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-war-is-in-the-dance-a-comprehensive-rakan-guide-593159',
        },
        'Blitzcrank': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-17-hanjaros-blitzcrank-guide-552851',
        },
        'Soraka': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-16-bizzleberrys-season-13-soraka-guide-543705',
        },
        'Janna': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-7-eiensieis-guide-to-janna-support-566687',
        },
        'Taric': {
            'support': 'https://www.mobafire.com/league-of-legends/build/13-15-1300lp-challenger-taric-jungle-welcome-to-the-gemshow-553457',
        }
    }   

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name}')

@bot.command()
async def build(ctx, champion_name, lane):
    champion_name = champion_name.capitalize()
    lane = lane.lower()
    
    # Sprawdzenie, czy linia jest prawidłowa
    available_lanes = ['top', 'jungle', 'mid', 'bot', 'support']
    if lane not in available_lanes:
        await ctx.send(f'Podano nieprawidłową linię. Dostępne linie: {", ".join(available_lanes)}.')
        return
    
    if champion_name in builds:
        if lane in builds[champion_name]:
            mobafire_url = builds[champion_name][lane]
            await ctx.send(f'Build dla {champion_name} na linii {lane}:\n{mobafire_url}')
        else:
            await ctx.send('Nie znaleziono danych dla podanej linii.')
    else:
        await ctx.send('Nie znaleziono danych dla podanego bohatera.')

@bot.command()
async def losujbohatera(ctx):
    available_champions = list(builds.keys())
    random_champion = random.choice(available_champions)
    
    await ctx.send(f'Wylosowany bohater: {random_champion}')
    
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    
    await ctx.send('Proszę wybierz linię (np. top, jungle, mid, bot, support):')
    try:
        lane_message = await bot.wait_for('message', check=check, timeout=60)
        lane = lane_message.content.lower()
        
        if lane in builds[random_champion]:
            mobafire_url = builds[random_champion][lane]
            await ctx.send(f'Build dla {random_champion} na linii {lane}:\n{mobafire_url}')
        else:
            await ctx.send('Nie znaleziono danych dla podanej linii.')
    except TimeoutError:
        await ctx.send('Czas na wybór linii minął.')

@bot.command()
async def losujlinie(ctx):
    available_lanes = ['top', 'jungle', 'mid', 'bot', 'support']
    random_lane = random.choice(available_lanes)
    
    await ctx.send(f'Wylosowana linia: {random_lane}')
    
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    
    await ctx.send('Proszę wybierz postać spośród dostępnych:')
    try:
        champion_message = await bot.wait_for('message', check=check, timeout=60)
        champion_name = champion_message.content.capitalize()
        
        if champion_name in builds:
            if random_lane in builds[champion_name]:
                mobafire_url = builds[champion_name][random_lane]
                await ctx.send(f'Build dla {champion_name} na linii {random_lane}:\n{mobafire_url}')
            else:
                await ctx.send(f'Wybrana postać ({champion_name}) nie jest dostępna na wylosowanej linii ({random_lane}).')
        else:
            await ctx.send(f'Nie znaleziono danych dla wybranej postaci: {champion_name}.')
    except TimeoutError:
        await ctx.send('Czas na wybór postaci minął.')

@bot.command()
async def losuj4fun(ctx):
    available_champions = list(builds.keys())
    random_champion = random.choice(available_champions)
    
    await ctx.send(f'Wylosowany bohater: {random_champion}')
    
    available_lanes = ['top', 'jungle', 'mid', 'bot', 'support']
    available_lanes.remove(random.choice(list(builds[random_champion].keys())))
    random_lane = random.choice(available_lanes)
    
    await ctx.send(f'Wylosowana linia (nieprzeznaczona dla {random_champion}): {random_lane}')
    
    available_builds = []
    for champ_name, champ_builds in builds.items():
        if champ_name != random_champion:
            available_builds.extend(champ_builds.values())
    random_build = random.choice(available_builds)
    
    await ctx.send(f'Wylosowany build (nieprzeznaczony dla {random_champion}): {random_build}')

@bot.command()
async def ulubieni(ctx, champion_name, lane, build_link):
    champion_name = champion_name.capitalize()
    lane = lane.lower()
    
    available_lanes = ['top', 'jungle', 'mid', 'bot', 'support']
    if lane not in available_lanes:
        await ctx.send(f'Podano nieprawidłową linię. Dostępne linie: {", ".join(available_lanes)}.')
        return
    
    if champion_name in builds:
        if lane in builds[champion_name]:
            ulubieni[ctx.author.id] = ulubieni.get(ctx.author.id, {})
            ulubieni[ctx.author.id][champion_name] = {'lane': lane, 'build_link': build_link}
            await ctx.send(f'Dodano bohatera {champion_name} na linię {lane} z buildem: {build_link} do ulubionych.')
        else:
            await ctx.send('Nie znaleziono danych dla podanej linii.')
    else:
        await ctx.send('Nie znaleziono danych dla podanego bohatera.')

@bot.command()
async def ulubienilista(ctx):
    if ctx.author.id in ulubieni:
        favorite_champions = ulubieni[ctx.author.id]
        if favorite_champions:
            await ctx.send('Twoi ulubieni bohaterowie:')
            for champ, data in favorite_champions.items():
                await ctx.send(f'Bohater: {champ}, Linia: {data["lane"]}, Build: {data["build_link"]}')
        else:
            await ctx.send('Nie masz ulubionych bohaterów.')
    else:
        await ctx.send('Nie masz ulubionych bohaterów.')


bot.run(TOKEN)
