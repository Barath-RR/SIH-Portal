function openCity(evt, name) {
    var home_section = document.querySelector('.home-section');
    var problem_statement_creation = document.querySelector('.psc');
    var problem_statement_view = document.querySelector('.psv');
    var nodal_officer = document.querySelector('.nodal-officer');

    if(name === "db") {
      home_section.style.removeProperty('display');
      problem_statement_creation.style.display = "none";
      problem_statement_view.style.display = "none";
      nodal_officer.style.display = "none";
    } else if(name === 'psc') {
      home_section.style.display = "none";
      problem_statement_creation.style.display = "flex";
      problem_statement_view.style.display = "none";
      nodal_officer.style.display = "none";
    } else if(name === 'vps') {
      home_section.style.display = "none";
      problem_statement_creation.style.display = "none";
      problem_statement_view.style.display = "flex";
      nodal_officer.style.display = "none";
    } else if(name === "nodalofficer") {
      home_section.style.display = "none";
      problem_statement_view.style.display = "none";
      problem_statement_creation.style.display = "none";
      nodal_officer.style.display = "flex";
    }
}