/** @type {import('next').NextConfig} */
const nextConfig = {
    basePath: '/app',
    assetPrefix: '/app/',
    webpack: (config, _) => ({
        ...config,
        watchOptions: {
          ...config.watchOptions,
          poll: 800,
          aggregateTimeout: 300
        }
     })
}

module.exports = nextConfig
