import jsminifier
import readmebuilder


def main(filename):
    jsminifier.minify(filename)
    readmebuilder.build(filename)


if __name__ == '__main__':
    main("event-emitter.js")
