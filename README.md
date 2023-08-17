# banana_llm_research

- [x] scraper
    - get first 10 models from each leaderboard
        - can do seperate file for each the leaderboards
        - if file is executed it returns desired data
- [x] create simple html page
    - ascii headline and description in header - 
    - render white gradio table as i frame in html
    - rendet all three tables correctly arranged
    - overall design of tables 
- [x] get feedback    
- [ ] deploy --> not possible to do vercel 
    - cannot make vercel account
- [x] add four columns with coming sxon (Try API, Try Playground, Cost 100 tokens/sec, How to setup?) - 
    - fix issue of lmysys coming soon stuff
- [x] add mission statement on top<>
- [ ] tell what i would improve in the user experience
- [ ] create first template for vicuna 13B
    - i think this might be really important 
    - i can just create the 




i need to add 

i am going to setup a bunch of models. 

the user experience for deploying a model from a template was flawlesy besides this two issues it would have took me 10 minutes to have a model running in under two minutes. thats great! only way to make this faster would be performance when building the docker i guess.  

i am just thinking of an feature request ... on the page https://app.banana.dev/deploy it would be nice to have a 

 


## mvp banana llm research dashboard

- name of project = banana llm research
- support for following leaderboards (biggest / most supported in the web)
    - https://chat.lmsys.org/?arena
    - https://huggingface.co/spaces/huggingfaceh4/open_llm_leaderboard
    ~~ - https://tatsu-lab.github.io/alpaca_eval/ ~~
- render them on a simple html page
    - scraping
        - a scraper that runs once a day for aggregating all data
        - an algorithm that checks if the model is open source and if yes, takes it (for commercial ones we cannot create a playground etc for banana)?
    - every leaderboard gets its own section with the name of the leaderboard as the headline and provided link
    - two dashboards in one row
- columns (columns which are additionally added to all)
    - already provided columns are displayed
    - costs (needs more engineering so that it makes sense)
        - option 1:
            - on top of the page, it's possible to configure how costs are calculated
                - gpu
                - tokens streamed per hour?
                - requests sent per hour?
        - option 2:
            - fixed configuration chosen
            - gpu size so that even the biggest model could fit?
            - fixed token stream per hour
            - fixed requests
    - link to playground
    - link to run it as an api
    - link to blog post