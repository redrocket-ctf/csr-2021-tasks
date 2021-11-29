# --------------> The build image
FROM node:lts AS build

WORKDIR /usr/src/app
COPY package*.json /usr/src/app/
RUN npm ci --only=production

# --------------> The production image
FROM node:lts-alpine

EXPOSE 3000
WORKDIR /usr/src/app
ENV NODE_ENV production

# Add the necessary files
COPY --chown=node:node --from=build /usr/src/app/node_modules /usr/src/app/node_modules
COPY --chown=node:node . /usr/src/app

# Add session folder
RUN mkdir -p /usr/src/app/sessions
# Set permissions to revoke write access
RUN chmod -R 555 /usr/src/app
# Allow read/write access on the session folder
RUN chmod -R 777 sessions
# Revoke write access on the flag
RUN chmod 444 flag.txt && chown root:root flag.txt

# To remove in prod version
RUN npm install -g nodemon

# Set default user for container
USER node

CMD ["npm", "run", "dev"]