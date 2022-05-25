---
layout: page
title: Projects
nav_order: 2
---

# Current Projects

{% for project in site.projects %}

<div class="card" style="margin: 9px">
  <div class="card-body">
    <div class="row">
      <div class="col-5">
        <a href="https://github.com/{{site.github_username}}/{{project.repo_name}}" class="btn btn-primary"><i class="fa fa-github"></i> {{ project.name }} - {{project.last_version}}</a> 
      </div>
      <div class="col-4 align-text-bottom">Last tagged {{project.last_published}}</div> 
      <div class="col-3"> 
        <a data-bs-toggle="collapse" href="#{{project.name}}Description" role="button" aria-expanded="false" aria-controls="#{{project.name}}Description" class="btn btn-info">Show Description</a>
      </div>
    </div>
    <div class="row">
        <div class="col">
        <div class="collapse multi-collapse" id="{{project.name}}Description" style="margin: 11px">
            <div class="card card-body">
                {{ project.readme }}
            </div>
        </div>
        </div>
    </div>
  </div>
</div>

{% endfor %}


# Prospective Projects

{% for prosp_project in site.prospective_projects %}

<div class="card" style="margin: 9px">
  <div class="card-body">
    <div class="row">
    <div class="col-10">
    <a href="{{prosp_project.issue_url}}" class="btn btn-primary"><i class="fa fa-github"></i> {{ prosp_project.title }}</a> 
    </div>
    <div class="col-2"> {% if prosp_project.report_link.size > 1 %}
    <a href="{{prosp_project.report_link}}" class="btn btn-link">Report</a>
    {% endif %}
    </div>
    </div>
  </div>
</div>

{% endfor %}