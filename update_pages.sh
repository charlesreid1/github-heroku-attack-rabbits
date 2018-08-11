#!/bin/bash

# These must be mkdocs sites!
REPOS="
bots/boring-mind-machine
bots/embarcadero-mind-machine
bots/rainbow-mind-machine
bots/russian-rainbow-mind-machine

docker/d-gitea
docker/d-mediawiki
docker/d-mysql
docker/d-nginx-charlesreid1
docker/d-nginx-subdomains
docker/d-phpmyadmin
docker/d-python-files
docker/d-python-helium

docker/pod-bots
docker/pod-charlesreid1
docker/pod-webhooks

charlesreid1/git-commit-ectomy
charlesreid1/github-heroku-attack-rabbits
charlesreid1/how-do-i-heroku
charlesreid1/how-do-i-pandoc
charlesreid1/how-do-i-pelican
charlesreid1/how-do-i-pyenv
charlesreid1/how-do-i-snakemake

charlesreid1/search-demo-mkdocs-material
charlesreid1/translate-yer-docs
charlesreid1/uncle-archie
charlesreid1/wisko-manual
"

function update_mkdocs_submodule() {

    for repo in ${REPOS}; do
        echo "Working on repo ${repo}"
        git clone --recursive -b master ssh://git@git.charlesreid1.com:222/${repo}
        rn=""
        rn=$(echo ${repo} | cut -d/ -f2)
        cd ${rn}

        cd mkdocs-material
        git checkout master
        git pull origin master
        cd ../

        git add mkdocs-material
        git commit mkdocs-material -m 'Update mkdocs-material submodule for mkdocs 1.0'

        sed -i 's/^pages:/nav:/' mkdocs.yml
        if [ "$(grep "nav" mkdocs.yml)" != "" ]; then
            echo -en '\n\nstrict: true\n' >> mkdocs.yml
        fi
    
        git add mkdocs.yml
        git commit mkdocs.yml -m 'Update mkdocs.yml for mkdocs 1.0'

        git push origin master
        cd ../
        ###rm -fr ${rn}
    done
}

main
