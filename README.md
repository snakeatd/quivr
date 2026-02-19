# odonto-ufro - Your Second Brain, Empowered by Generative AI

<div align="center">
    <img src="./logo.png" alt="odonto-ufro-logo" width="30%"  style="border-radius: 50%; padding-bottom: 20px"/>
</div>

[![Discord Follow](https://dcbadge.vercel.app/api/server/HUpRgp2HG8?style=flat)](https://discord.gg/HUpRgp2HG8)
[![GitHub Repo stars](https://img.shields.io/github/stars/snakeatd/odonto-ufro?style=social)](https://github.com/snakeatd/odonto-ufro)
[![Twitter Follow](https://img.shields.io/twitter/follow/StanGirard?style=social)](https://twitter.com/_StanGirard)

odonto-ufro, your second brain, utilizes the power of GenerativeAI to be your personal assistant ! Think of it as Obsidian, but turbocharged with AI capabilities.

## Key Features 🎯

- **Fast and Efficient**: Designed with speed and efficiency at its core. odonto-ufro ensures rapid access to your data.
- **Secure**: Your data, your control. Always.
- **OS Compatible**: Ubuntu 22 or newer.
- **File Compatibility**: Text, Markdown, PDF, Powerpoint, Excel, CSV, Word, Audio, Video
- **Open Source**: Freedom is beautiful, and so is odonto-ufro. Open source and free to use.
- **Public/Private**: Share your brains with your users via a public link, or keep them private.
- **Marketplace**: Share your brains with the world, or use other people's brains to boost your productivity.
- **Offline Mode**: odonto-ufro works offline, so you can access your data anytime, anywhere.

## Demo Highlights 🎥

https://github.com/snakeatd/odonto-ufro/assets/19614572/a6463b73-76c7-4bc0-978d-70562dca71f5

## Getting Started 🚀

You can deploy odonto-ufro to Porter Cloud with one-click:

<a href="https://cloud.porter.run/addons/new?addon_name=odonto-ufro" target="_blank">
  <img src="https://mintlify.s3-us-west-1.amazonaws.com/porter/images/deploying-applications/deploy-to-porter.svg" alt="Deploy to Porter" style="width: 150px;">
</a>


If you would like to deploy locally, follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

You can find everything on the [documentation](https://docs.quivr.app/).

### Prerequisites 📋

Ensure you have the following installed:

- Docker
- Docker Compose

### 60 seconds Installation 💽

You can find the installation video [here](https://www.youtube.com/watch?v=cXBa6dZJN48).

- **Step 0**: Supabase CLI

  Follow the instructions [here](https://supabase.com/docs/guides/cli/getting-started) to install the Supabase CLI that is required.

  ```bash
  supabase -v # Check that the installation worked
  ```


- **Step 1**: Clone the repository:

  ```bash
  git clone https://github.com/snakeatd/odonto-ufro.git && cd odonto-ufro
  ```

- **Step 2**: Copy the `.env.example` files

  ```bash
  cp .env.example .env
  ```

- **Step 3**: Update the `.env` files

  ```bash
  vim .env # or emacs or vscode or nano
  ```

  Update **OPENAI_API_KEY** in the `.env` file.

  You just need to update the `OPENAI_API_KEY` variable in the `.env` file. You can get your API key [here](https://platform.openai.com/api-keys). You need to create an account first. And put your credit card information. Don't worry, you won't be charged unless you use the API. You can find more information about the pricing [here](https://openai.com/pricing/).


- **Step 4**: Launch the project

  ```bash
  cd backend && supabase start
  ```
  and then 
  ```bash
  cd ../
  docker compose pull
  docker compose up
  ```

  If you have a Mac, go to Docker Desktop > Settings > General and check that the "file sharing implementation" is set to `VirtioFS`.

  If you are a developer, you can run the project in development mode with the following command: `docker compose -f docker-compose.dev.yml up --build`

- **Step 5**: Login to the app

  You can now sign in to the app with `admin@odonto-ufro.app` & `admin`. You can access the app at [http://localhost:3000/login](http://localhost:3000/login).

  You can access odonto-ufro backend API at [http://localhost:5050/docs](http://localhost:5050/docs)

  You can access supabase at [http://localhost:54323](http://localhost:54323)

## Updating odonto-ufro 🚀

- **Step 1**: Pull the latest changes

  ```bash
  git pull
  ```

- **Step 2**: Update the migration

  ```bash
  supabase migration up
  ```


## Contributors ✨

Thanks go to these wonderful people:
<a href="https://github.com/snakeatd/odonto-ufro/graphs/contributors">
<img src="https://contrib.rocks/image?repo=snakeatd/odonto-ufro" />
</a>

## Contribute 🤝

Did you get a pull request? Open it, and we'll review it as soon as possible. Check out our project board [here](https://github.com/users/StanGirard/projects/5) to see what we're currently focused on, and feel free to bring your fresh ideas to the table!

- [Open Issues](https://github.com/snakeatd/odonto-ufro/issues)
- [Open Pull Requests](https://github.com/snakeatd/odonto-ufro/pulls)
- [Good First Issues](https://github.com/snakeatd/odonto-ufro/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)
- [Frontend Issues](https://github.com/snakeatd/odonto-ufro/issues?q=is%3Aopen+is%3Aissue+label%3Afrontend)
- [Backend Issues](https://github.com/snakeatd/odonto-ufro/issues?q=is%3Aopen+is%3Aissue+label%3Abackend)

## Partners ❤️

This project would not be possible without the support of our partners. Thank you for your support!


<a href="https://ycombinator.com/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Y_Combinator_logo.svg/1200px-Y_Combinator_logo.svg.png" alt="YCombinator" style="padding: 10px" width="70px">
</a>
<a href="https://www.theodo.fr/">
  <img src="https://avatars.githubusercontent.com/u/332041?s=200&v=4" alt="Theodo" style="padding: 10px" width="70px">
</a>

## License 📄

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details

## Stars History 📈

[![Star History Chart](https://api.star-history.com/svg?repos=snakeatd/odonto-ufro&type=Timeline)](https://star-history.com/#snakeatd/odonto-ufro&Timeline)
