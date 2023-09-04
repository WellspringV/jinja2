{% set error = 'Программа не установлена' %}
Имя компьютера: {{hostvars[inventory_hostname]['ansible_facts']['fqdn']}}
Сетевой адрес компьютера: {{hostvars[inventory_hostname]['ansible_facts']['default_ipv4']['address']}}
{% if hostvars[inventory_hostname]['ansible_facts']['packages']['vim'] is defined %}
Vim версия: {{hostvars[inventory_hostname]['ansible_facts']['packages']['vim'][0].version}}
{% else %}
Vim версия: {{error}}
{% endif %}
{% if hostvars[inventory_hostname]['ansible_facts']['packages']['chromium'] is defined %}
chromium версия: {{hostvars[inventory_hostname]['ansible_facts']['packages']['chromium'][0].version}}
{% else %}
chromium версия: {{error}}
{% endif %}
