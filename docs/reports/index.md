---
layout: page
title: Reports
permalink: /reports/
has_children: true
nav_order: 5
has_toc: false
---
# Reports

<div class="accordion" id="labelAccordion">

{% for label in site.labels %}

<div class="accordion-item">
    <h2 class="accordion-header" id="heading{{label.id_}}">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse{{label.id_}}" aria-expanded="true" aria-controls="collapse{{label.id_}}">
        {{ label.title }}
        </button>
    </h2>
    <div id="collapse{{label.id_}}" class="accordion-collapse collapse" aria-labelledby="heading{{label.id_}}" data-bs-parent="#labelAccordion">
        <div class="accordion-body">
        <strong>{{ label.description }}</strong>
        {% include issue_report_list.html issues=label.issues %}
        </div>
    </div>
</div>
{% endfor %}
</div>
