import { XMarkIcon } from '@heroicons/react/20/solid'


interface Props {
    online: boolean;
}

export const OnlineBanner = (props: Props) => {
  return (
    <>
      {/*
        Make sure you add some bottom padding to pages that include a sticky banner like this to prevent
        your content from being obscured when the user scrolls to the bottom of the page.
      */}
        {props.online !== true && (
            <div className="pointer-events-none fixed inset-x-0 bottom-0 sm:flex sm:justify-center sm:px-6 sm:pb-5 lg:px-8">
                <div className="pointer-events-auto flex items-center justify-between gap-x-6 bg-gray-900 px-6 py-2.5 sm:rounded-xl sm:py-3 sm:pl-4 sm:pr-3.5">
                    <p className="text-sm leading-6 text-white">
                        System is Offline
                    </p>
                </div>
            </div>
        )}

    </>
  )
}
