#!/usr/bin/env python3

import random



def banners():
    hdrs = ['''

                        ░█▀▀░█░█░█▀▄░▀█▀░▀█▀░▀█▀░█░░░█▀▀░█▀▀░░░░░█▀▄░█░░
                        ░▀▀█░█░█░█▀▄░░█░░░█░░░█░░█░░░█▀▀░▀▀█░▄▄▄░█░█░█░░
                        ░▀▀▀░▀▀▀░▀▀░░░▀░░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀░░░░░▀▀░░▀▀▀''',


            '''
                                          ▌  ▐  ▗▐  ▜            ▌▜
                                    ▞▀▘▌ ▌▛▀▖▜▀ ▄▜▀ ▐ ▞▀▖▞▀▘▄▄▖▞▀▌▐
                                    ▝▀▖▌ ▌▌ ▌▐ ▖▐▐ ▖▐ ▛▀ ▝▀▖   ▌ ▌▐
                                    ▀▀ ▝▀▘▀▀  ▀ ▀▘▀  ▘▝▀▘▀▀    ▝▀▘ ▘''',

            '''

                              ▗▖          █       ▗▄▖                    ▗▖▗▄▖
                              ▐▌    ▐▌    ▀   ▐▌  ▝▜▌                    ▐▌▝▜▌
                    ▗▟██▖▐▌ ▐▌▐▙█▙ ▐███  ██  ▐███  ▐▌   ▟█▙ ▗▟██▖      ▟█▟▌ ▐▌
                    ▐▙▄▖▘▐▌ ▐▌▐▛ ▜▌ ▐▌    █   ▐▌   ▐▌  ▐▙▄▟▌▐▙▄▖▘     ▐▛ ▜▌ ▐▌
                     ▀▀█▖▐▌ ▐▌▐▌ ▐▌ ▐▌    █   ▐▌   ▐▌  ▐▛▀▀▘ ▀▀█▖ ██▌ ▐▌ ▐▌ ▐▌
                    ▐▄▄▟▌▐▙▄█▌▐█▄█▘ ▐▙▄ ▗▄█▄▖ ▐▙▄  ▐▙▄ ▝█▄▄▌▐▄▄▟▌     ▝█▄█▌ ▐▙▄
                     ▀▀▀  ▀▀▝▘▝▘▀▘   ▀▀ ▝▀▀▀▘  ▀▀   ▀▀  ▝▀▀  ▀▀▀       ▝▀▝▘  ▀▀ ''',



            '''
                                    ▐    ▗   ▝   ▗  ▝▜                ▐ ▝▜
                             ▄▖ ▗ ▗ ▐▄▖ ▗▟▄ ▗▄  ▗▟▄  ▐   ▄▖  ▄▖      ▄▟  ▐
                            ▐ ▝ ▐ ▐ ▐▘▜  ▐   ▐   ▐   ▐  ▐▘▐ ▐ ▝     ▐▘▜  ▐
                             ▀▚ ▐ ▐ ▐ ▐  ▐   ▐   ▐   ▐  ▐▀▀  ▀▚  ▀▘ ▐ ▐  ▐
                            ▝▄▞ ▝▄▜ ▐▙▛  ▝▄ ▗▟▄  ▝▄  ▝▄ ▝▙▞ ▝▄▞     ▝▙█  ▝▄ ''',

            '''
                                    ╔═╝║ ║╔═ ═╔╝╝═╔╝║  ╔═╝╔═╝  ╔═ ║
                                    ══║║ ║╔═║ ║ ║ ║ ║  ╔═╝══║═╝║ ║║
                                    ══╝══╝══  ╝ ╝ ╝ ══╝══╝══╝  ══ ══╝''',

            '''
                                    ┏━┛┃ ┃┏━ ━┏┛┛━┏┛┃  ┏━┛┏━┛  ┏━ ┃
                                    ━━┃┃ ┃┏━┃ ┃ ┃ ┃ ┃  ┏━┛━━┃━┛┃ ┃┃
                                    ━━┛━━┛━━  ┛ ┛ ┛ ━━┛━━┛━━┛  ━━ ━━┛''',

            '''
                                    ┏━┓╻ ╻┏┓ ╺┳╸╻╺┳╸╻  ┏━╸┏━┓   ╺┳┓╻
                                    ┗━┓┃ ┃┣┻┓ ┃ ┃ ┃ ┃  ┣╸ ┗━┓╺━╸ ┃┃┃
                                    ┗━┛┗━┛┗━┛ ╹ ╹ ╹ ┗━╸┗━╸┗━┛   ╺┻┛┗━╸''',
           ]

    print("\n\n{}\n\n".format(random.choice(hdrs)))


if __name__ == '__main__':
    banners()
