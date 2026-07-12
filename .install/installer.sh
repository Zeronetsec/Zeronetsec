function install::installer() {
    if [[ "${__BACKUP__}" == true && -d "${opt}/zeronetsec" ]]; then
        (
            cd "${opt}"
            install::getinstall \
                "
                    command zip -r \
                        zeronetsec_${bkdate}.bak.zip \
                        zeronetsec
                " \
                "Backup: ${GG}${opt}/zeronetsec ${DG}-> ${GG}${opt}/zeronetsec_${bkdate}.bak.zip${N}"
            cd
        )
    fi

    if [[ -d "${opt}/zeronetsec" ]]; then
        install::getinstall \
            "command rm -rf ${opt}/zeronetsec" \
            "Removing old source..."
    fi

    install::getinstall \
        "command mv ${root} ${opt}/zeronetsec" \
        "Moving: ${GG}${root} ${DG}-> ${GG}${opt}/zeronetsec${N}"

    install::getinstall \
        "command chmod +x ${opt}/zeronetsec/zeronetsec.py" \
        "Set permission for: ${GG}${opt}/zeronetsec/zeronetsec.py${N}"

    install::getinstall \
        "
            command ln -sf \
                ${opt}/zeronetsec/zeronetsec.py \
                ${bin}/zeronetsec
        " \
        "Symlink: ${GG}${opt}/zeronetsec/zeronetsec.py ${DG}-> ${GG}${bin}/zeronetsec${N}"
}; readonly -f install::installer