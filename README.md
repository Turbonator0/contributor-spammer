# Setup
Set your origin to your repository with the structure of http://USER:TOKEN@github.com/your/repository

# Use

```
python3 ./spammer.py <count>
```
count is used to determine how many commits to generate before pushing

## Use with a slick one liner

```bash
for i in {1,10}; do python3 ./spammer.py 1000; done
```
This way you bypass the limit of 1000 per push for contributions
